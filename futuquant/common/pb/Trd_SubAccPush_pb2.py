# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Trd_SubAccPush.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Common_pb2 as Common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Trd_SubAccPush.proto',
  package='Trd_SubAccPush',
  syntax='proto2',
  serialized_pb=_b('\n\x14Trd_SubAccPush.proto\x12\x0eTrd_SubAccPush\x1a\x0c\x43ommon.proto\"\x14\n\x03\x43\x32S\x12\r\n\x05\x61\x63\x63ID\x18\x01 \x03(\x04\"\x05\n\x03S2C\"+\n\x07Request\x12 \n\x03\x63\x32s\x18\x01 \x02(\x0b\x32\x13.Trd_SubAccPush.C2S\"o\n\x08Response\x12 \n\x07retType\x18\x01 \x02(\x0e\x32\x0f.Common.RetType\x12\x0e\n\x06retMsg\x18\x02 \x01(\t\x12\x0f\n\x07\x65rrCode\x18\x03 \x01(\x05\x12 \n\x03s2c\x18\x04 \x01(\x0b\x32\x13.Trd_SubAccPush.S2C')
  ,
  dependencies=[Common__pb2.DESCRIPTOR,])




_C2S = _descriptor.Descriptor(
  name='C2S',
  full_name='Trd_SubAccPush.C2S',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='accID', full_name='Trd_SubAccPush.C2S.accID', index=0,
      number=1, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=74,
)


_S2C = _descriptor.Descriptor(
  name='S2C',
  full_name='Trd_SubAccPush.S2C',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=81,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Trd_SubAccPush.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='c2s', full_name='Trd_SubAccPush.Request.c2s', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=83,
  serialized_end=126,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Trd_SubAccPush.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='retType', full_name='Trd_SubAccPush.Response.retType', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='retMsg', full_name='Trd_SubAccPush.Response.retMsg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errCode', full_name='Trd_SubAccPush.Response.errCode', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='s2c', full_name='Trd_SubAccPush.Response.s2c', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=128,
  serialized_end=239,
)

_REQUEST.fields_by_name['c2s'].message_type = _C2S
_RESPONSE.fields_by_name['retType'].enum_type = Common__pb2._RETTYPE
_RESPONSE.fields_by_name['s2c'].message_type = _S2C
DESCRIPTOR.message_types_by_name['C2S'] = _C2S
DESCRIPTOR.message_types_by_name['S2C'] = _S2C
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

C2S = _reflection.GeneratedProtocolMessageType('C2S', (_message.Message,), dict(
  DESCRIPTOR = _C2S,
  __module__ = 'Trd_SubAccPush_pb2'
  # @@protoc_insertion_point(class_scope:Trd_SubAccPush.C2S)
  ))
_sym_db.RegisterMessage(C2S)

S2C = _reflection.GeneratedProtocolMessageType('S2C', (_message.Message,), dict(
  DESCRIPTOR = _S2C,
  __module__ = 'Trd_SubAccPush_pb2'
  # @@protoc_insertion_point(class_scope:Trd_SubAccPush.S2C)
  ))
_sym_db.RegisterMessage(S2C)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'Trd_SubAccPush_pb2'
  # @@protoc_insertion_point(class_scope:Trd_SubAccPush.Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'Trd_SubAccPush_pb2'
  # @@protoc_insertion_point(class_scope:Trd_SubAccPush.Response)
  ))
_sym_db.RegisterMessage(Response)


# @@protoc_insertion_point(module_scope)
