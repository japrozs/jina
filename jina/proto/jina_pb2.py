# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: jina.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import docarray.proto.docarray_pb2 as docarray__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\njina.proto\x12\x04jina\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x0e\x64ocarray.proto\"\x9f\x01\n\nRouteProto\x12\x10\n\x08\x65xecutor\x18\x01 \x01(\t\x12.\n\nstart_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12!\n\x06status\x18\x04 \x01(\x0b\x32\x11.jina.StatusProto\"\xc6\x01\n\x0bHeaderProto\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12!\n\x06status\x18\x02 \x01(\x0b\x32\x11.jina.StatusProto\x12\x1a\n\rexec_endpoint\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x1c\n\x0ftarget_executor\x18\x04 \x01(\tH\x01\x88\x01\x01\x12\x14\n\x07timeout\x18\x05 \x01(\rH\x02\x88\x01\x01\x42\x10\n\x0e_exec_endpointB\x12\n\x10_target_executorB\n\n\x08_timeout\"#\n\x0e\x45ndpointsProto\x12\x11\n\tendpoints\x18\x01 \x03(\t\"\xf9\x01\n\x0bStatusProto\x12*\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x1c.jina.StatusProto.StatusCode\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x33\n\texception\x18\x03 \x01(\x0b\x32 .jina.StatusProto.ExceptionProto\x1aN\n\x0e\x45xceptionProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x61rgs\x18\x02 \x03(\t\x12\x0e\n\x06stacks\x18\x03 \x03(\t\x12\x10\n\x08\x65xecutor\x18\x04 \x01(\t\"$\n\nStatusCode\x12\x0b\n\x07SUCCESS\x10\x00\x12\t\n\x05\x45RROR\x10\x01\"^\n\rRelatedEntity\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\r\x12\x15\n\x08shard_id\x18\x04 \x01(\rH\x00\x88\x01\x01\x42\x0b\n\t_shard_id\"\xa0\x02\n\x10\x44\x61taRequestProto\x12!\n\x06header\x18\x01 \x01(\x0b\x32\x11.jina.HeaderProto\x12+\n\nparameters\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12 \n\x06routes\x18\x03 \x03(\x0b\x32\x10.jina.RouteProto\x12\x35\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\'.jina.DataRequestProto.DataContentProto\x1a\x63\n\x10\x44\x61taContentProto\x12,\n\x04\x64ocs\x18\x01 \x01(\x0b\x32\x1c.docarray.DocumentArrayProtoH\x00\x12\x14\n\ndocs_bytes\x18\x02 \x01(\x0cH\x00\x42\x0b\n\tdocuments\"@\n\x14\x44\x61taRequestListProto\x12(\n\x08requests\x18\x01 \x03(\x0b\x32\x16.jina.DataRequestProto2Z\n\x12JinaDataRequestRPC\x12\x44\n\x0cprocess_data\x12\x1a.jina.DataRequestListProto\x1a\x16.jina.DataRequestProto\"\x00\x32\x63\n\x18JinaSingleDataRequestRPC\x12G\n\x13process_single_data\x12\x16.jina.DataRequestProto\x1a\x16.jina.DataRequestProto\"\x00\x32G\n\x07JinaRPC\x12<\n\x04\x43\x61ll\x12\x16.jina.DataRequestProto\x1a\x16.jina.DataRequestProto\"\x00(\x01\x30\x01\x32`\n\x18JinaDiscoverEndpointsRPC\x12\x44\n\x12\x65ndpoint_discovery\x12\x16.google.protobuf.Empty\x1a\x14.jina.EndpointsProto\"\x00\x62\x06proto3')



_ROUTEPROTO = DESCRIPTOR.message_types_by_name['RouteProto']
_HEADERPROTO = DESCRIPTOR.message_types_by_name['HeaderProto']
_ENDPOINTSPROTO = DESCRIPTOR.message_types_by_name['EndpointsProto']
_STATUSPROTO = DESCRIPTOR.message_types_by_name['StatusProto']
_STATUSPROTO_EXCEPTIONPROTO = _STATUSPROTO.nested_types_by_name['ExceptionProto']
_RELATEDENTITY = DESCRIPTOR.message_types_by_name['RelatedEntity']
_DATAREQUESTPROTO = DESCRIPTOR.message_types_by_name['DataRequestProto']
_DATAREQUESTPROTO_DATACONTENTPROTO = _DATAREQUESTPROTO.nested_types_by_name['DataContentProto']
_DATAREQUESTLISTPROTO = DESCRIPTOR.message_types_by_name['DataRequestListProto']
_STATUSPROTO_STATUSCODE = _STATUSPROTO.enum_types_by_name['StatusCode']
RouteProto = _reflection.GeneratedProtocolMessageType('RouteProto', (_message.Message,), {
  'DESCRIPTOR' : _ROUTEPROTO,
  '__module__' : 'jina_pb2'
  # @@protoc_insertion_point(class_scope:jina.RouteProto)
  })
_sym_db.RegisterMessage(RouteProto)

HeaderProto = _reflection.GeneratedProtocolMessageType('HeaderProto', (_message.Message,), {
  'DESCRIPTOR' : _HEADERPROTO,
  '__module__' : 'jina_pb2'
  # @@protoc_insertion_point(class_scope:jina.HeaderProto)
  })
_sym_db.RegisterMessage(HeaderProto)

EndpointsProto = _reflection.GeneratedProtocolMessageType('EndpointsProto', (_message.Message,), {
  'DESCRIPTOR' : _ENDPOINTSPROTO,
  '__module__' : 'jina_pb2'
  # @@protoc_insertion_point(class_scope:jina.EndpointsProto)
  })
_sym_db.RegisterMessage(EndpointsProto)

StatusProto = _reflection.GeneratedProtocolMessageType('StatusProto', (_message.Message,), {

  'ExceptionProto' : _reflection.GeneratedProtocolMessageType('ExceptionProto', (_message.Message,), {
    'DESCRIPTOR' : _STATUSPROTO_EXCEPTIONPROTO,
    '__module__' : 'jina_pb2'
    # @@protoc_insertion_point(class_scope:jina.StatusProto.ExceptionProto)
    })
  ,
  'DESCRIPTOR' : _STATUSPROTO,
  '__module__' : 'jina_pb2'
  # @@protoc_insertion_point(class_scope:jina.StatusProto)
  })
_sym_db.RegisterMessage(StatusProto)
_sym_db.RegisterMessage(StatusProto.ExceptionProto)

RelatedEntity = _reflection.GeneratedProtocolMessageType('RelatedEntity', (_message.Message,), {
  'DESCRIPTOR' : _RELATEDENTITY,
  '__module__' : 'jina_pb2'
  # @@protoc_insertion_point(class_scope:jina.RelatedEntity)
  })
_sym_db.RegisterMessage(RelatedEntity)

DataRequestProto = _reflection.GeneratedProtocolMessageType('DataRequestProto', (_message.Message,), {

  'DataContentProto' : _reflection.GeneratedProtocolMessageType('DataContentProto', (_message.Message,), {
    'DESCRIPTOR' : _DATAREQUESTPROTO_DATACONTENTPROTO,
    '__module__' : 'jina_pb2'
    # @@protoc_insertion_point(class_scope:jina.DataRequestProto.DataContentProto)
    })
  ,
  'DESCRIPTOR' : _DATAREQUESTPROTO,
  '__module__' : 'jina_pb2'
  # @@protoc_insertion_point(class_scope:jina.DataRequestProto)
  })
_sym_db.RegisterMessage(DataRequestProto)
_sym_db.RegisterMessage(DataRequestProto.DataContentProto)

DataRequestListProto = _reflection.GeneratedProtocolMessageType('DataRequestListProto', (_message.Message,), {
  'DESCRIPTOR' : _DATAREQUESTLISTPROTO,
  '__module__' : 'jina_pb2'
  # @@protoc_insertion_point(class_scope:jina.DataRequestListProto)
  })
_sym_db.RegisterMessage(DataRequestListProto)

_JINADATAREQUESTRPC = DESCRIPTOR.services_by_name['JinaDataRequestRPC']
_JINASINGLEDATAREQUESTRPC = DESCRIPTOR.services_by_name['JinaSingleDataRequestRPC']
_JINARPC = DESCRIPTOR.services_by_name['JinaRPC']
_JINADISCOVERENDPOINTSRPC = DESCRIPTOR.services_by_name['JinaDiscoverEndpointsRPC']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ROUTEPROTO._serialized_start=129
  _ROUTEPROTO._serialized_end=288
  _HEADERPROTO._serialized_start=291
  _HEADERPROTO._serialized_end=489
  _ENDPOINTSPROTO._serialized_start=491
  _ENDPOINTSPROTO._serialized_end=526
  _STATUSPROTO._serialized_start=529
  _STATUSPROTO._serialized_end=778
  _STATUSPROTO_EXCEPTIONPROTO._serialized_start=662
  _STATUSPROTO_EXCEPTIONPROTO._serialized_end=740
  _STATUSPROTO_STATUSCODE._serialized_start=742
  _STATUSPROTO_STATUSCODE._serialized_end=778
  _RELATEDENTITY._serialized_start=780
  _RELATEDENTITY._serialized_end=874
  _DATAREQUESTPROTO._serialized_start=877
  _DATAREQUESTPROTO._serialized_end=1165
  _DATAREQUESTPROTO_DATACONTENTPROTO._serialized_start=1066
  _DATAREQUESTPROTO_DATACONTENTPROTO._serialized_end=1165
  _DATAREQUESTLISTPROTO._serialized_start=1167
  _DATAREQUESTLISTPROTO._serialized_end=1231
  _JINADATAREQUESTRPC._serialized_start=1233
  _JINADATAREQUESTRPC._serialized_end=1323
  _JINASINGLEDATAREQUESTRPC._serialized_start=1325
  _JINASINGLEDATAREQUESTRPC._serialized_end=1424
  _JINARPC._serialized_start=1426
  _JINARPC._serialized_end=1497
  _JINADISCOVERENDPOINTSRPC._serialized_start=1499
  _JINADISCOVERENDPOINTSRPC._serialized_end=1595
# @@protoc_insertion_point(module_scope)
