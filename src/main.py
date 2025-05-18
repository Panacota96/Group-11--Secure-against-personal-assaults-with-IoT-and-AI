# Install all required libraries for the src folder
# Run this in your terminal:
# pip install -r src\requirements.txt

from audioSample import record_audio
from audioAlert import play_audio
from sendMessage import send_sms, send_email, notify_user
from sendMessage import KID_NAME
import os
#from threatDetection import is_threat
from voiceRecognition import recognize_speech, is_matching_speaker, get_reference_embedding

# Example usage of imported functions:

if __name__ == "__main__":
    
    # Ask the user if there is a heart anomaly detected on the screen
    user_input = input("Is there a heart anomaly detected on the screen? (yes/no): ")
    if user_input.strip().lower() == "yes":
        print("Heart anomaly detected. Initiating alert sequence.")
        # 1. Play an alert audio (provide a valid path to an mp3 file)
        play_audio('AlertMessage/alert.mp3')
        # 2. Record audio sample
        audio_file = record_audio(duration=5, sample_rate=44100, folder='test_samples', channels=2)

        
    

        # 3. Send an SMS and Email (make sure .env is configured)
        # Example SMS
        sms_msg = f"ALERT: {KID_NAME} is in Danger!"
        notify_user("sms", os.getenv("PARENT_PHONE"), sms_msg)

        # Example Email
        subject = f"ALERT: {KID_NAME} is in Danger!"
        body    = (
            f"Attention,\n\n"
            f"{KID_NAME} may be in danger. Please check their status immediately.\n\n"
            "— Your Alert System"
        )
        notify_user("email", os.getenv("PARENT_EMAIL"), subject, body)


        # 4. Threat detection on a sample text
        #text = "I will attack you tonight"
        #print(f"Threat detected: {is_threat(text)}")

        # 5. Voice recognition and speaker verification (provide valid audio paths)
        # ref_embedding = get_reference_embedding("reference/reference_person.wav")
        # recognized_text = recognize_speech(audio_file)
        # print(f"Recognized Text: {recognized_text}")
        # is_match = is_matching_speaker(audio_file, ref_embedding)
        # print(f"Is the same person? {'✅ Yes' if is_match else '❌ No'}")
    else:
        print("No heart anomaly detected.")
    
    


