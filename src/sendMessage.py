#2  To send an SMS, we’ll use Twilio. For email, we’ll use smtplib and a Gmail SMTP server.
#3  Make sure to install the required libraries:
# pip install twilio
#4  You also need to enable "Less secure app access" in your Gmail account settings or use an App Password if you have 2FA enabled.
#5  This script will send an SMS or an email based on the method you choose.
#6  Make sure to replace the placeholders with your actual credentials.
#7  This script is a simple example and does not include error handling or logging for production use.
import smtplib
from email.mime.text import MIMEText
from twilio.rest import Client

# --- CONFIGURATION ---
# Fill these with your info
TWILIO_SID = 'TWILIO_SID'
TWILIO_AUTH_TOKEN = 'TWILIO_Token'
TWILIO_PHONE_NUMBER = 'TWILLIO_Phone_number'  # Your Twilio phone number
GMAIL_USER = 'your_email@gmail.com'
GMAIL_PASSWORD = 'your_app_password'
KID_NAME= 'John Doe'  # Replace with the actual kid's name

# --- SEND SMS ---
def send_sms(to_number, message):
    try:
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=to_number
        )
        print(f"SMS sent to {to_number}: SID {message.sid}")
    except Exception as e:
        print(f"Failed to send SMS: {e}")

# --- SEND EMAIL ---
def send_email(to_email, subject, message):
    try:
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = GMAIL_USER
        msg['To'] = to_email

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(GMAIL_USER, GMAIL_PASSWORD)
            server.send_message(msg)
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# --- MAIN FUNCTION ---
def notify_user(method, recipient, subject_or_message, message=None):
    if method == 'sms':
        send_sms(recipient, subject_or_message)
    elif method == 'email':
        send_email(recipient, subject_or_message, message)
    else:
        print("Unsupported method. Use 'sms' or 'email'.")


if __name__ == "__main__":
    # SMS example
    notify_user('sms', '+33774929723', 'ALERT: {KID_NAME} is in Danger!')

    # Email example
    # notify_user('email', 'recipient@example.com', 'Test Subject', 'This is the email body.')
    pass
