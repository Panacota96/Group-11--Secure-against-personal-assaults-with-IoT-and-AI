import sounddevice as sd
from scipy.io.wavfile import write
import os
from datetime import datetime

"""
    Records audio from the default microphone and saves it to the specified folder.
    
    Args:
        duration (int): Duration of recording in seconds.
        sample_rate (int): Sample rate in Hz.
        folder (str): Folder where the audio file will be saved.
        channels (int): Number of audio channels (e.g., 1 for mono, 2 for stereo).
        
    Returns:
        str: Path to the saved audio file.
"""

def record_audio(duration=5, sample_rate=44100, folder='audio_samples', channels=2):
    
    # Create folder if it doesn't exist
    if not os.path.exists(folder):
        os.makedirs(folder)


    # Record audio
    print(f"Recording for {duration} seconds with {channels} channel(s)...")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels, dtype='int16')
    sd.wait()  # Wait until recording is finished
    print("Recording finished.")

    # Save audio to file
    filename = datetime.now().strftime("%Y%m%d_%H%M%S") + '.wav'
    file_path = os.path.join(folder, filename)
    write(file_path, sample_rate, audio_data)

    print(f"Audio saved to {file_path}")
    return file_path

if __name__ == "__main__":
    # Example usage of the record_audio function
    duration = 10  # Duration in seconds
    sample_rate = 44100  # Sample rate in Hz
    folder = 'test_samples'  # Folder to save the audio file
    # Call the record_audio function
    record_audio(duration=duration, sample_rate=sample_rate, folder=folder)
