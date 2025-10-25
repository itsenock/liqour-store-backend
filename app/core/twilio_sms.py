import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_number = os.getenv("TWILIO_PHONE_NUMBER")

client = Client(account_sid, auth_token)

def send_sms(phone: str, message: str):
    try:
        message = client.messages.create(
            body=message,
            from_=twilio_number,
            to=phone
        )
        print("Twilio SMS sent:", message.sid)
    except Exception as e:
        print("Twilio SMS failed:", str(e))
