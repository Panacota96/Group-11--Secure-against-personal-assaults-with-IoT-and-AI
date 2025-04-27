import os
import pygame


def play_audio(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return

    # Initialize pygame mixer
    pygame.mixer.init()

    # Load and play the audio file
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        print(f"Playing: {file_path}")
        
        # Wait for the audio to finish playing
        while pygame.mixer.music.get_busy():
            continue
    except pygame.error as e:
        print(f"Error playing audio: {e}")
    finally:
        pygame.mixer.quit()

# Example usage
if __name__ == "__main__":
    folder_path = "AlertMessage"
    # Look for the first audio file in the folder
    audio_file = None
    for file in os.listdir(folder_path):
        if file.endswith(".mp3"):  # You can add more extensions if needed
            audio_file = file
            break

    if not audio_file:
        print(f"No audio file found in folder: {folder_path}")
        exit()
    file_path = os.path.join(folder_path, audio_file)
    play_audio(file_path)