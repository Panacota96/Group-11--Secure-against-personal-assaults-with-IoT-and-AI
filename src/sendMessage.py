import os
import logging
from pathlib import Path
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from twilio.rest import Client

"""
sendMessage.py
This module provides functionality to send notifications via SMS (using Twilio) and email (using Gmail SMTP).
It loads configuration from a .env file, sets up logging, and defines utility functions for sending messages.
Functions:
    send_sms(to_number: str, message: str) -> None
        Sends an SMS message to the specified phone number using Twilio API.
    send_email(to_email: str, subject: str, body: str) -> None
        Sends an email to the specified address using Gmail SMTP with an App Password.
    notify_user(method: str, recipient: str, subject_or_message: str, body: str = None)
        Dispatches a notification to the user via the specified method ('sms' or 'email').
Environment Variables (loaded from data.env):
    TWILIO_SID           - Twilio Account SID
    TWILIO_AUTH_TOKEN    - Twilio Auth Token
    TWILIO_PHONE_NUMBER  - Twilio phone number to send SMS from
    GMAIL_USER           - Gmail address to send emails from
    GMAIL_APP_PASSWORD   - Gmail App Password for SMTP authentication
    KID_NAME             - Name of the child (used in alert messages)
    PARENT_PHONE         - Parent's phone number (for SMS alerts)
    PARENT_EMAIL         - Parent's email address (for email alerts)
Example Usage:
    Run the script directly to send example SMS and email alerts using the configured environment variables.
"""




# Load environment variables from Twillio/data.env
# ────── LOAD CONFIG ──────
env_path = Path(__file__).parent /"data.env"
load_dotenv(dotenv_path=env_path)

print(f"env_path: {env_path}")

# Twilio config
TWILIO_SID         = os.getenv("TWILIO_SID") 
TWILIO_AUTH_TOKEN  = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE       = os.getenv("TWILIO_PHONE_NUMBER")

# Gmail config
GMAIL_USER         = os.getenv("GMAIL_USER")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")

# Misc
KID_NAME           = os.getenv("KID_NAME", "Unknown")

# ────── LOGGING SETUP ──────
logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ────── SMS SENDER ──────
def send_sms(to_number: str, message: str) -> None:
    """Send an SMS via Twilio."""
    try:
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        msg = client.messages.create(
            body=message,
            from_=TWILIO_PHONE,
            to=to_number
        )
        logger.info(f"SMS sent to {to_number} (SID: {msg.sid})")
    except Exception as e:
        logger.exception(f"Failed to send SMS to {to_number}")

# ────── EMAIL SENDER ──────
def send_email(to_email: str, subject: str, body: str) -> None:
    """Send an email via Gmail SMTP SSL using an App Password."""
    try:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"]    = GMAIL_USER
        msg["To"]      = to_email

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(GMAIL_USER, GMAIL_APP_PASSWORD)
            smtp.send_message(msg)
            logger.info(f"Email sent to {to_email}")
    except Exception as e:
        logger.exception(f"Failed to send email to {to_email}")

# ────── NOTIFICATION DISPATCHER ──────
def notify_user(method: str, recipient: str, subject_or_message: str, body: str = None):
    method = method.lower()
    if method == "sms":
        send_sms(recipient, subject_or_message)
    elif method == "email":
        if body is None:
            logger.error("Body is required for email notifications.")
            return
        send_email(recipient, subject_or_message, body)
    else:
        logger.error("Unsupported method. Use 'sms' or 'email'.")

# ────── MAIN EXECUTION ──────
if __name__ == "__main__":
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
