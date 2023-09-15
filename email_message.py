"""Module for creating an email."""
from __future__ import annotations

import base64
from email.message import EmailMessage
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailHeaders: # pylint: disable=too-few-public-methods
    """Headers for the Email."""
    to_address: str
    from_address: str
    subject: str
    reply_to_address: str | None
    cc: str | None
    bcc: str | None

    def __init__( # pylint: disable=too-many-arguments
        self,
        to_address: str,
        from_address: str,
        subject: str,
        reply_to_address: str | None = None,
        cc: str | None = None, # pylint: disable=invalid-name
        bcc: str | None = None
    ) -> None:
        self.to_address = to_address
        self.from_address = from_address
        self.reply_to_address = reply_to_address
        self.cc = cc # pylint: disable=invalid-name
        self.bcc = bcc
        self.subject = subject

    def __str__(self) -> str:
        return (
            f"to: {self.to_address}\n" +
            f"from: {self.from_address}\n" +
            f"reply_to: {self.reply_to_address}\n" +
            f"subject: {self.subject}\n" +
            f"cc: {self.cc}\n" +
            f"bcc: {self.bcc}\n" +
            f"subject: {self.subject}"
        )

class Email:
    """Class representing an Email.
    Used to convert to IMF format using email.Message.EmailMessage.
    """
    _headers: EmailHeaders
    _body_text: str
    _body_html: str | None
    _message: MIMEBase

    def __init__(
        self,
        headers: EmailHeaders,
        body_text: str,
        body_html: str | None
    ) -> None:
        self._headers = headers
        self._body_text = body_text
        self._body_html = body_html

        # Covert data for transport
        if self._body_html:
            self._create_mime_alternative()
        else:
            self._create_email_message()

    def _create_mime_alternative(self) -> None:
        # https://docs.python.org/3/library/email.message.html
        self._message = MIMEMultipart('alternative')

        text_mime = MIMEText(self._body_text, 'plain')
        self._message.attach(text_mime)

        mime_html = MIMEText(self._body_html, 'html')
        self._message.attach(mime_html)

        self._set_headers()

    def _create_email_message(self) -> None:
        # https://docs.python.org/3/library/email.message.html
        self._message = EmailMessage()
        self._message.set_content(self._body_text)

        self._set_headers()

    def _set_headers(self) -> None:
        # See RFC 5322: 3.6
        # https://datatracker.ietf.org/doc/html/rfc5322.html#section-3.6
        self._message['to'] = self._headers.to_address

        if self._headers.cc:
            self._message['cc'] = self._headers.cc
        if self._headers.bcc:
            self._message['bcc'] = self._headers.bcc
        if self._headers.reply_to_address:
            self._message['reply_to'] = self._headers.reply_to_address

        self._message['from'] = self._headers.from_address
        self._message['subject'] = self._headers.subject

    def __str__(self) -> str:
        return str(self._headers)

    def base64encode(self) -> str:
        """Encodes IMF message to base64"""
        # encoded message
        message_bytes: bytes = self._message.as_bytes()
        return base64.urlsafe_b64encode(message_bytes).decode()
