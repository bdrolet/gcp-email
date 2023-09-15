"""Module for sending emails through gmail."""
from __future__ import annotations
from __future__ import print_function

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.auth import default, iam
from google.auth.transport import requests
from google.oauth2 import service_account

from google.oauth2 import service_account
from email_message import Email
from email_message import EmailHeaders
from send_email_pb2 import SendEmail
from dotenv import load_dotenv

import sys
import os

load_dotenv()
TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
GSUITE_ADMIN_USER = os.getenv('GSUITE_ADMIN_USER')
SCOPES: list[str] = [
    # https://developers.google.com/gmail/api/auth/scopes#gmail_scopes
    'https://www.googleapis.com/auth/gmail.send'
]
SERVICE_ACCOUNT_FILE = os.getenv('GMAIL_SERVICE_ACCOUNT_FILE')

def send_message(
    send_email_proto: SendEmail
) -> None:
    """Sends the Email through gmail."""
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(f"Current directory: {dir_path}")
    creds = _get_service_account()

    email: Email = Email(
        headers=EmailHeaders(
            to_address=",".join(send_email_proto.to_address),
            from_address=send_email_proto.from_address,
            cc=",".join(send_email_proto.cc_address),
            bcc=",".join(send_email_proto.bcc_address),
            reply_to_address=send_email_proto.reply_to_address,
            subject=send_email_proto.subject
        ),
        body_text=send_email_proto.text,
        body_html=None
        # body_html=send_email_proto.HasField('html') ? message.html : None
    )

    try:
        # Call the Gmail API
        # https://developers.google.com/gmail/api/reference/rest
        # service = build('gmail', 'v1', credentials=creds)
        service = build('gmail', 'v1', credentials=creds)

        # https://developers.google.com/gmail/api/reference/rest/v1/users.messages#Message
        message: dict[str, str] = {
            'labelIds': ['sent_from_script'],
            'raw': email.base64encode()
        }
        print(f"Sending message: {email} through Gmail...")

        # https://developers.google.com/gmail/api/reference/rest/v1/users.messages/send
        sent_message = (
            service.users().messages().send( # pylint: disable=no-member
                userId="me",
                body=message
            ).execute()
        )
        print(f"Sent message through gmail: {sent_message}")

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')


def _get_service_account() -> Credentials:
    # Gets the service account from file.
    # See this post for details...
    # https://developers.google.com/identity/protocols/oauth2/service-account#python
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    return creds.with_subject(GSUITE_ADMIN_USER)

if __name__ == '__main__':
    to_address = sys.argv[1]
    send_email_proto: SendEmail = SendEmail(
        from_address=GSUITE_ADMIN_USER,
        to_address=[to_address],
        subject='Test from local script',
        text='Hello...'
    )
    send_message(send_email_proto=send_email_proto)