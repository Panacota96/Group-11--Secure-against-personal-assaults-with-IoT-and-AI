import os
import numpy as np
import librosa
import torch
import torchaudio
import torch.nn.functional as F
from torchaudio.pipelines import WAV2VEC2_BASE, SQUIM_OBJECTIVE
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
"""
voiceRecognition.py
This module provides functions for speaker verification, speech quality assessment, and automatic speech recognition (ASR) using pre-trained models from torchaudio and Hugging Face Transformers. It enables comparison of speaker embeddings, assessment of audio quality, transcription of speech to text, and detection of safe words in transcriptions.
Functions:
    extract_embedding(audio_path):
        Extracts a speaker embedding from an audio file using a pre-trained Wav2Vec2 model.
    compare_embeddings(embedding1, embedding2, threshold=0.7):
        Compares two speaker embeddings using cosine similarity and returns whether they are considered the same speaker.
    assess_quality(audio_path):
        Assesses the quality of a speech audio file using the SQUIM model and returns quality metrics.
    transcribe_audio(audio_path):
        Transcribes speech from an audio file to text using a pre-trained Wav2Vec2 ASR model.
    detect_safe_word(transcription, safe_word="help"):
        Checks if a specified safe word is present in the transcription.
    is_same_speaker(audio_path1, audio_path2, safe_word="help"):
        Main function that compares two audio files for speaker similarity, assesses their quality, transcribes the second audio, and detects the safe word.
Example Usage:
    Run the module as a script to compare two audio files, assess their quality, transcribe the test sample, and detect the presence of a safe word.
"""


# Load Wav2Vec2 pre-trained model
bundle = WAV2VEC2_BASE
model = bundle.get_model().eval()

# Load SQUIM model from the official bundle
squim_model = SQUIM_OBJECTIVE.get_model().eval()

# Load the ASR model and processor
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
asr_model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h").eval()

# Function to extract speaker embedding
def extract_embedding(audio_path):
    waveform, sample_rate = torchaudio.load(audio_path)
    if sample_rate != bundle.sample_rate:
        waveform = torchaudio.functional.resample(waveform, sample_rate, bundle.sample_rate)
    with torch.inference_mode():
        features, _ = model.extract_features(waveform)
    embedding = features[-1].mean(dim=1).squeeze()  # shape: (feature_dim,)
    return embedding

# Function to compare two embeddings using PyTorch cosine similarity
def compare_embeddings(embedding1, embedding2, threshold=0.7):
    emb1 = embedding1 if isinstance(embedding1, torch.Tensor) else torch.tensor(embedding1, dtype=torch.float32)
    emb2 = embedding2 if isinstance(embedding2, torch.Tensor) else torch.tensor(embedding2, dtype=torch.float32)
    emb1 = emb1.flatten()
    emb2 = emb2.flatten()
    min_len = min(emb1.shape[-1], emb2.shape[-1])
    emb1 = emb1[..., :min_len]
    emb2 = emb2[..., :min_len]
    dot = torch.dot(emb1, emb2)
    norm1 = emb1.norm()
    norm2 = emb2.norm()
    similarity = (dot / (norm1 * norm2)).item()
    return similarity >= threshold, similarity

# Function to assess speech quality
def assess_quality(audio_path):
    waveform, sample_rate = torchaudio.load(audio_path)
    if sample_rate != 16000:
        waveform = torchaudio.functional.resample(waveform, sample_rate, 16000)
    with torch.inference_mode():
        metrics = squim_model(waveform)
    return metrics

# Function to transcribe audio to text
def transcribe_audio(audio_path):
    waveform, sample_rate = torchaudio.load(audio_path)
    if sample_rate != 16000:
        waveform = torchaudio.functional.resample(waveform, sample_rate, 16000)
    # Ensure mono audio
    if waveform.shape[0] > 1:
        waveform = waveform.mean(dim=0, keepdim=True)
    input_values = processor(waveform.squeeze(), sampling_rate=16000, return_tensors="pt").input_values
    with torch.inference_mode():
        logits = asr_model(input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.batch_decode(predicted_ids)[0].lower()
    return transcription

# Function to detect safe word in transcription
def detect_safe_word(transcription, safe_word="help"):
    return safe_word.lower() in transcription

# Main function
def is_same_speaker(audio_path1, audio_path2, safe_word="help"):
    embedding1 = extract_embedding(audio_path1)
    embedding2 = extract_embedding(audio_path2)
    is_same, similarity = compare_embeddings(embedding1, embedding2)
    quality1 = assess_quality(audio_path1)
    quality2 = assess_quality(audio_path2)
    transcription = transcribe_audio(audio_path2)
    safe_word_detected = detect_safe_word(transcription, safe_word)
    return is_same, similarity, quality1, quality2, transcription, safe_word_detected

# Example usage
if __name__ == "__main__":
    audio1 = "reference/reference_person.wav"
    audio2 = "test_samples/test_sample.wav"
    same, score, quality1, quality2, transcription, safe_word_detected = is_same_speaker(audio1, audio2)
    print(f"Same Speaker: {same}, Similarity Score: {score:.4f}")
    print(f"Quality Score 1: {quality1}")
    print(f"Quality Score 2: {quality2}")
    print(f"Transcription: {transcription}")
    print(f"Safe Word Detected: {safe_word_detected}")