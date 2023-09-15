import os
import requests
import sys
from send_email_pb2 import SendEmail
from dotenv import load_dotenv

load_dotenv()

DOMAIN: str = os.getenv('MAILGUN_DOMAIN')
API_KEY: str = os.getenv('MAILGUN_API_KEY')
GSUITE_ADMIN_USER = os.getenv('GSUITE_ADMIN_USER')


def send_email(send_email_proto: SendEmail) -> None:
    """Sends a message to mailgun"""
    
    # Sending to MailGun API
    resp = requests.post(
        f"https://api.mailgun.net/v3/{DOMAIN}/messages",
        auth=("api", API_KEY),
        data={
            "from": send_email_proto.from_address,
            "to": send_email_proto.to_address,
            "subject": send_email_proto.subject,
            "text": send_email_proto.text
        }
    )
    print(f"response from Mailgun: {resp}")

if __name__ == '__main__':
    to_address: str = sys.argv[1]
    send_email_proto: SendEmail = SendEmail(
        from_address=GSUITE_ADMIN_USER,
        to_address=[to_address],
        subject='Test mg send from local script',
        text='Hello...'
    )
    send_email(send_email_proto=send_email_proto)