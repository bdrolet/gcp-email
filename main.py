"""Module for sending email via mailgun"""
from __future__ import annotations

import functions_framework
from cloudevents.http import CloudEvent
from google.protobuf.json_format import Parse
import base64
import send_email_pb2
import gmail_send


@functions_framework.cloud_event
def send_message(cloud_event: CloudEvent) -> None:
    # Loading message from cloud_event
    data = base64.b64decode(cloud_event.data["message"]["data"]).decode()
    message = send_email_pb2.SendEmail()
    Parse(text=data, message=message)

    gmail_send.send_message(send_email_proto=message)

