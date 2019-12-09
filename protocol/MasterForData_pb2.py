# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: MasterForData.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='MasterForData.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13MasterForData.proto\"\x11\n\x03Num\x12\n\n\x02id\x18\x01 \x01(\x05\"\"\n\x06socket\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\";\n\x0frecommitRequest\x12\x0b\n\x03\x46ID\x18\x01 \x01(\x05\x12\x0b\n\x03\x43ID\x18\x02 \x01(\x05\x12\x0e\n\x06status\x18\x03 \x01(\x05\"$\n\x10recommitResponse\x12\x10\n\x08isCommit\x18\x01 \x01(\x08\x32Z\n\x03MFD\x12 \n\rRegisteServer\x12\x07.socket\x1a\x04.Num\"\x00\x12\x31\n\x08Recommit\x12\x10.recommitRequest\x1a\x11.recommitResponse\"\x00\x62\x06proto3')
)




_NUM = _descriptor.Descriptor(
  name='Num',
  full_name='Num',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Num.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=40,
)


_SOCKET = _descriptor.Descriptor(
  name='socket',
  full_name='socket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='socket.ip', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='socket.port', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=42,
  serialized_end=76,
)


_RECOMMITREQUEST = _descriptor.Descriptor(
  name='recommitRequest',
  full_name='recommitRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='FID', full_name='recommitRequest.FID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='CID', full_name='recommitRequest.CID', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='recommitRequest.status', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=78,
  serialized_end=137,
)


_RECOMMITRESPONSE = _descriptor.Descriptor(
  name='recommitResponse',
  full_name='recommitResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='isCommit', full_name='recommitResponse.isCommit', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=175,
)

DESCRIPTOR.message_types_by_name['Num'] = _NUM
DESCRIPTOR.message_types_by_name['socket'] = _SOCKET
DESCRIPTOR.message_types_by_name['recommitRequest'] = _RECOMMITREQUEST
DESCRIPTOR.message_types_by_name['recommitResponse'] = _RECOMMITRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Num = _reflection.GeneratedProtocolMessageType('Num', (_message.Message,), {
  'DESCRIPTOR' : _NUM,
  '__module__' : 'MasterForData_pb2'
  # @@protoc_insertion_point(class_scope:Num)
  })
_sym_db.RegisterMessage(Num)

socket = _reflection.GeneratedProtocolMessageType('socket', (_message.Message,), {
  'DESCRIPTOR' : _SOCKET,
  '__module__' : 'MasterForData_pb2'
  # @@protoc_insertion_point(class_scope:socket)
  })
_sym_db.RegisterMessage(socket)

recommitRequest = _reflection.GeneratedProtocolMessageType('recommitRequest', (_message.Message,), {
  'DESCRIPTOR' : _RECOMMITREQUEST,
  '__module__' : 'MasterForData_pb2'
  # @@protoc_insertion_point(class_scope:recommitRequest)
  })
_sym_db.RegisterMessage(recommitRequest)

recommitResponse = _reflection.GeneratedProtocolMessageType('recommitResponse', (_message.Message,), {
  'DESCRIPTOR' : _RECOMMITRESPONSE,
  '__module__' : 'MasterForData_pb2'
  # @@protoc_insertion_point(class_scope:recommitResponse)
  })
_sym_db.RegisterMessage(recommitResponse)



_MFD = _descriptor.ServiceDescriptor(
  name='MFD',
  full_name='MFD',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=177,
  serialized_end=267,
  methods=[
  _descriptor.MethodDescriptor(
    name='RegisteServer',
    full_name='MFD.RegisteServer',
    index=0,
    containing_service=None,
    input_type=_SOCKET,
    output_type=_NUM,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Recommit',
    full_name='MFD.Recommit',
    index=1,
    containing_service=None,
    input_type=_RECOMMITREQUEST,
    output_type=_RECOMMITRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MFD)

DESCRIPTOR.services_by_name['MFD'] = _MFD

# @@protoc_insertion_point(module_scope)
