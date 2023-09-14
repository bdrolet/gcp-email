from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SendEmail(_message.Message):
    __slots__ = ["from_address", "reply_to_address", "to_address", "cc_address", "bcc_address", "subject", "text", "html"]
    FROM_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    REPLY_TO_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TO_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BCC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    HTML_FIELD_NUMBER: _ClassVar[int]
    from_address: str
    reply_to_address: str
    to_address: _containers.RepeatedScalarFieldContainer[str]
    cc_address: _containers.RepeatedScalarFieldContainer[str]
    bcc_address: _containers.RepeatedScalarFieldContainer[str]
    subject: str
    text: str
    html: str
    def __init__(self, from_address: _Optional[str] = ..., reply_to_address: _Optional[str] = ..., to_address: _Optional[_Iterable[str]] = ..., cc_address: _Optional[_Iterable[str]] = ..., bcc_address: _Optional[_Iterable[str]] = ..., subject: _Optional[str] = ..., text: _Optional[str] = ..., html: _Optional[str] = ...) -> None: ...
