# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: InventoryRecord.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15InventoryRecord.proto\"$\n\x16InventoryRecordRequest\x12\n\n\x02id\x18\x01 \x01(\t\"C\n\x1cInventoryRecordRequestSearch\x12\x10\n\x08key_name\x18\x01 \x01(\t\x12\x11\n\tkey_value\x18\x02 \x01(\t\"\\\n\x1aInventoryRecordSearchRange\x12\x10\n\x08key_name\x18\x01 \x01(\t\x12\x15\n\rkey_value_min\x18\x02 \x01(\x02\x12\x15\n\rkey_value_max\x18\x03 \x01(\x02\"7\n\x0fGetDistribution\x12\x10\n\x08key_name\x18\x01 \x01(\t\x12\x12\n\npercentile\x18\x02 \x01(\x01\"B\n\x15UpdateInventoryRecord\x12)\n\x0finventoryRecord\x18\x01 \x01(\x0b\x32\x10.InventoryRecord\"D\n\x17InventoryRecordResponse\x12)\n\x0finventoryRecord\x18\x01 \x01(\x0b\x32\x10.InventoryRecord\"-\n\x1bInventoryRecordBoolResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08\"H\n\x1bInventoryRecordResponseList\x12)\n\x0finventoryRecord\x18\x01 \x03(\x0b\x32\x10.InventoryRecord\".\n\x15InventoryAtPercentile\x12\x15\n\rat_percentile\x18\x01 \x01(\x01\"\xe7\x01\n\x0fInventoryRecord\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x11\n\tunitPrice\x18\x04 \x01(\x02\x12\x17\n\x0fquantityInStock\x18\x05 \x01(\x05\x12\x17\n\x0finveneotryValue\x18\x06 \x01(\x02\x12\x14\n\x0creorderLevel\x18\x07 \x01(\x05\x12\x19\n\x11reorderTimeInDays\x18\x08 \x01(\x05\x12\x19\n\x11quantityInReorder\x18\t \x01(\x05\x12\x14\n\x0c\x64iscontinued\x18\n \x01(\x08\x32\xb0\x03\n\x16InventoryRecordService\x12M\n\x16getInventoryRecordById\x12\x17.InventoryRecordRequest\x1a\x18.InventoryRecordResponse\"\x00\x12Y\n\x1cgetInventoryRecordByKeyValue\x12\x1d.InventoryRecordRequestSearch\x1a\x18.InventoryRecordResponse\"\x00\x12`\n!getInventoryRecordByKeyValueRange\x12\x1b.InventoryRecordSearchRange\x1a\x1c.InventoryRecordResponseList\"\x00\x12=\n\x0fgetDistribution\x12\x10.GetDistribution\x1a\x16.InventoryAtPercentile\"\x00\x12K\n\x15updateInventoryRecord\x12\x16.UpdateInventoryRecord\x1a\x18.InventoryRecordResponse\"\x00\x42@\n io.grpc.examples.InventoryRecordB\x14InventoryRecordProtoP\x01\xa2\x02\x03RTGb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'InventoryRecord_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n io.grpc.examples.InventoryRecordB\024InventoryRecordProtoP\001\242\002\003RTG'
  _globals['_INVENTORYRECORDREQUEST']._serialized_start=25
  _globals['_INVENTORYRECORDREQUEST']._serialized_end=61
  _globals['_INVENTORYRECORDREQUESTSEARCH']._serialized_start=63
  _globals['_INVENTORYRECORDREQUESTSEARCH']._serialized_end=130
  _globals['_INVENTORYRECORDSEARCHRANGE']._serialized_start=132
  _globals['_INVENTORYRECORDSEARCHRANGE']._serialized_end=224
  _globals['_GETDISTRIBUTION']._serialized_start=226
  _globals['_GETDISTRIBUTION']._serialized_end=281
  _globals['_UPDATEINVENTORYRECORD']._serialized_start=283
  _globals['_UPDATEINVENTORYRECORD']._serialized_end=349
  _globals['_INVENTORYRECORDRESPONSE']._serialized_start=351
  _globals['_INVENTORYRECORDRESPONSE']._serialized_end=419
  _globals['_INVENTORYRECORDBOOLRESPONSE']._serialized_start=421
  _globals['_INVENTORYRECORDBOOLRESPONSE']._serialized_end=466
  _globals['_INVENTORYRECORDRESPONSELIST']._serialized_start=468
  _globals['_INVENTORYRECORDRESPONSELIST']._serialized_end=540
  _globals['_INVENTORYATPERCENTILE']._serialized_start=542
  _globals['_INVENTORYATPERCENTILE']._serialized_end=588
  _globals['_INVENTORYRECORD']._serialized_start=591
  _globals['_INVENTORYRECORD']._serialized_end=822
  _globals['_INVENTORYRECORDSERVICE']._serialized_start=825
  _globals['_INVENTORYRECORDSERVICE']._serialized_end=1257
# @@protoc_insertion_point(module_scope)
