# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: send_email.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10send_email.proto\"\xcd\x01\n\tSendEmail\x12\x14\n\x0c\x66rom_address\x18\x01 \x01(\t\x12\x1d\n\x10reply_to_address\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x12\n\nto_address\x18\x03 \x03(\t\x12\x12\n\ncc_address\x18\x04 \x03(\t\x12\x13\n\x0b\x62\x63\x63_address\x18\x05 \x03(\t\x12\x0f\n\x07subject\x18\x06 \x01(\t\x12\x0c\n\x04text\x18\x07 \x01(\t\x12\x11\n\x04html\x18\x08 \x01(\tH\x01\x88\x01\x01\x42\x13\n\x11_reply_to_addressB\x07\n\x05_htmlb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'send_email_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_SENDEMAIL']._serialized_start=21
  _globals['_SENDEMAIL']._serialized_end=226
# @@protoc_insertion_point(module_scope)
