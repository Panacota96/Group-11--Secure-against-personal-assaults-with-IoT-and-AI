# Install all required libraries for the src folder
# Run this in your terminal:
# pip install -r src\requirements.txt
import logging
from audioSample import record_audio
from audioAlert import play_audio
from sendMessage import send_sms, send_email, notify_user
from sendMessage import KID_NAME
import os
#from threatDetection import is_threat
from voiceRecognition import recognize_speech, is_matching_speaker, get_reference_embedding

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# Example usage of imported functions:

if __name__ == "__main__":
    
    # Ask the user if there is a heart anomaly detected on the screen
    user_input = input("Is there a heart anomaly detected on the screen? (yes/no): ")
    logger.debug("User input for heart anomaly: %s", user_input)
    if user_input.strip().lower() == "yes":
        logger.info("Heart anomaly detected. Initiating alert sequence.")
        # 1. Play an alert audio (provide a valid path to an mp3 file)
        try:
            play_audio('AlertMessage/alert.mp3')
            logger.info("Alert audio played successfully.")
        except Exception as e:
            logger.critical("Failed to play alert audio: %s", e)
        # 2. Record audio sample
        try:
            audio_file = record_audio(duration=5, sample_rate=44100, folder='test_samples', channels=2)
            logger.info("Audio sample recorded: %s", audio_file)
        except Exception as e:
            logger.critical("Failed to record audio: %s", e)
        
        # 3. Send an SMS and Email (make sure .env is configured)
        # Example SMS
        sms_msg = f"ALERT: {KID_NAME} is in Danger!"
        try:
            notify_user("sms", os.getenv("PARENT_PHONE"), sms_msg)
            logger.info("SMS notification sent.")
        except Exception as e:
            logger.critical("Failed to send SMS: %s", e)

        # Example Email
        subject = f"ALERT: {KID_NAME} is in Danger!"
        body    = (
            f"Attention,\n\n"
            f"{KID_NAME} may be in danger. Please check their status immediately.\n\n"
            "— Your Alert System"
        )
        try:
            notify_user("email", os.getenv("PARENT_EMAIL"), subject, body)
            logger.info("Email notification sent.")
        except Exception as e:
            logger.critical("Failed to send email: %s", e)


        # 4. Threat detection on a sample text
        #text = "I will attack you tonight"
        #try:
        #    threat = is_threat(text)
        #    if threat:
        #        logger.warning("Threat detected in text: %s", text)
        #    else:
        #        logger.info("No threat detected in text.")
        #except Exception as e:
        #    logger.critical("Threat detection failed: %s", e)

        # 5. Voice recognition and speaker verification (provide valid audio paths)
        #try:
        #    ref_embedding = get_reference_embedding("reference/reference_person.wav")
        #    recognized_text = recognize_speech(audio_file)
        #    logger.debug("Recognized Text: %s", recognized_text)
        #    is_match = is_matching_speaker(audio_file, ref_embedding)
        #    if is_match:
        #        logger.info("Speaker verified: same person.")
        #    else:
        #        logger.warning("Speaker verification failed: not the same person.")
        #except Exception as e:
        #    logger.critical("Voice recognition failed: %s", e)
    else:
        logger.info("No heart anomaly detected.")
        print("No heart anomaly detected.")




