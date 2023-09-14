"""Module for sending email via mailgun"""
from __future__ import annotations

import requests
import functions_framework
from cloudevents.http import CloudEvent
from google.protobuf.json_format import Parse
import base64
import os
import send_email_pb2

domain: str = 'sandboxe4caaed5b28d4847baef2e43b7d1e36c.mailgun.org'

@functions_framework.cloud_event
def send_message(cloud_event: CloudEvent) -> None:
    """Sends a message to mailgun"""
    api_key: str = os.getenv('MAILGUN_API_KEY')

    # Loading message from cloud_event
    data = base64.b64decode(cloud_event.data["message"]["data"]).decode()
    message = send_email_pb2.SendEmail()
    Parse(text=data, message=message)
    
    # Sending to MailGun API
    resp = requests.post(
        f"https://api.mailgun.net/v3/{domain}/messages",
        auth=("api", api_key),
        data={
            "from": message.from_address,
            "to": message.to_address,
            "subject": message.subject,
            "text": message.text
        }
    )
    print(f"response from Mailgun: {resp}")
