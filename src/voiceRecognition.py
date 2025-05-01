import os
import numpy as np
import speech_recognition as sr
from pyannote.audio import Inference

# 1. Speech Recognition
def recognize_speech(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError as e:
        return f"Error: {e}"

# 2. Speaker Identification
def is_matching_speaker(audio_file, reference_embedding, threshold=0.75):
    inference = Inference("pyannote/embedding", device="cpu")
    embedding = inference(audio_file)

    similarity = np.dot(embedding, reference_embedding) / (
        np.linalg.norm(embedding) * np.linalg.norm(reference_embedding)
    )
    print(f"Similarity Score: {similarity:.2f}")
    return similarity > threshold

# 3. Load reference voice
def get_reference_embedding(ref_audio_file):
    inference = Inference("pyannote/embedding", device="cpu")
    return inference(ref_audio_file)

if __name__ == "__main__":
    
    ##TODO Fill the reference folder and the test samples to test the code
    # Ensure the reference and test folders exist
    
    
    # Load reference embedding
    ref_embedding = get_reference_embedding("reference/reference_person.wav")

    # Test file
    test_file = "test_samples/test_sample.wav"

    # Speech Recognition
    recognized_text = recognize_speech(test_file)
    print(f"Recognized Text: {recognized_text}")

    # Speaker Check
    is_match = is_matching_speaker(test_file, ref_embedding)

    print(f"Is the same person? {'✅ Yes' if is_match else '❌ No'}")
