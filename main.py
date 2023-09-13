"""Module for sending email via mailgun"""
from __future__ import annotations

import requests
import functions_framework
from cloudevents.http import CloudEvent
domain: str = 'sandboxe4caaed5b28d4847baef2e43b7d1e36c.mailgun.org'
api_key: str = '5b886c620b4622bdbe1f994bb7842f65-413e373c-3938144f'

@functions_framework.cloud_event
def send_message(cloud_event: CloudEvent) -> None:
    """Sends a message to mailgun"""
    print(f"Received event with ID: {cloud_event['id']} and data {cloud_event.data}")
    
    requests.post(
        f"https://api.mailgun.net/v3/{domain}/messages",
        auth=("api", api_key),
        data={"from": f"server@{domain}",
              "to": ["ben@drolet.cloud"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})

# print(send_message())
