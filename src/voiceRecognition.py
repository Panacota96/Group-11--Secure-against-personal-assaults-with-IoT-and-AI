import os
import numpy as np
import librosa
import torch
import torchaudio
import torch.nn.functional as F
from torchaudio.pipelines import WAV2VEC2_BASE, SQUIM_OBJECTIVE

# Load Wav2Vec2 pre-trained model
bundle = WAV2VEC2_BASE
model = bundle.get_model().eval()

# Load SQUIM model from the official bundle
squim_model = SQUIM_OBJECTIVE.get_model().eval()

# Function to extract speaker embedding
def extract_embedding(audio_path):
    waveform, sample_rate = torchaudio.load(audio_path)
    if sample_rate != bundle.sample_rate:
        waveform = torchaudio.functional.resample(waveform, sample_rate, bundle.sample_rate)
    with torch.inference_mode():
        features, _ = model.extract_features(waveform)
    # Use the last layer, mean over time, return 1-D tensor
    embedding = features[-1].mean(dim=1).squeeze()  # shape: (feature_dim,)
    return embedding

# Function to compare two embeddings using PyTorch cosine similarity
def compare_embeddings(embedding1, embedding2, threshold=0.7):
    # Convert to torch tensors if needed
    emb1 = embedding1 if isinstance(embedding1, torch.Tensor) else torch.tensor(embedding1, dtype=torch.float32)
    emb2 = embedding2 if isinstance(embedding2, torch.Tensor) else torch.tensor(embedding2, dtype=torch.float32)
    # Flatten to 1D if needed
    emb1 = emb1.flatten()
    emb2 = emb2.flatten()
    # Truncate to same length
    min_len = min(emb1.shape[-1], emb2.shape[-1])
    emb1 = emb1[..., :min_len]
    emb2 = emb2[..., :min_len]
    # Compute cosine similarity manually
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

# Main function
def is_same_speaker(audio_path1, audio_path2):
    embedding1 = extract_embedding(audio_path1)
    embedding2 = extract_embedding(audio_path2)
    is_same, similarity = compare_embeddings(embedding1, embedding2)
    quality1 = assess_quality(audio_path1)
    quality2 = assess_quality(audio_path2)
    return is_same, similarity, quality1, quality2

# Example usage
if __name__ == "__main__":
    audio1 = "reference/reference_person.wav"
    audio2 = "test_samples/test_sample.wav"
    same, score, quality1, quality2 = is_same_speaker(audio1, audio2)
    print(f"Same Speaker: {same}, Similarity Score: {score:.4f}")
    print(f"Quality Score 1: {quality1}")
    print(f"Quality Score 2: {quality2}")
