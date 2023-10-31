from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InventoryRecordRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class InventoryRecordRequestSearch(_message.Message):
    __slots__ = ["key_name", "key_value"]
    KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    KEY_VALUE_FIELD_NUMBER: _ClassVar[int]
    key_name: str
    key_value: str
    def __init__(self, key_name: _Optional[str] = ..., key_value: _Optional[str] = ...) -> None: ...

class InventoryRecordSearchRange(_message.Message):
    __slots__ = ["key_name", "key_value_min", "key_value_max"]
    KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    KEY_VALUE_MIN_FIELD_NUMBER: _ClassVar[int]
    KEY_VALUE_MAX_FIELD_NUMBER: _ClassVar[int]
    key_name: str
    key_value_min: float
    key_value_max: float
    def __init__(self, key_name: _Optional[str] = ..., key_value_min: _Optional[float] = ..., key_value_max: _Optional[float] = ...) -> None: ...

class GetDistribution(_message.Message):
    __slots__ = ["key_name", "percentile"]
    KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    PERCENTILE_FIELD_NUMBER: _ClassVar[int]
    key_name: str
    percentile: float
    def __init__(self, key_name: _Optional[str] = ..., percentile: _Optional[float] = ...) -> None: ...

class UpdateInventoryRecord(_message.Message):
    __slots__ = ["inventoryRecord"]
    INVENTORYRECORD_FIELD_NUMBER: _ClassVar[int]
    inventoryRecord: InventoryRecord
    def __init__(self, inventoryRecord: _Optional[_Union[InventoryRecord, _Mapping]] = ...) -> None: ...

class InventoryRecordResponse(_message.Message):
    __slots__ = ["inventoryRecord"]
    INVENTORYRECORD_FIELD_NUMBER: _ClassVar[int]
    inventoryRecord: InventoryRecord
    def __init__(self, inventoryRecord: _Optional[_Union[InventoryRecord, _Mapping]] = ...) -> None: ...

class InventoryRecordBoolResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: bool = ...) -> None: ...

class InventoryRecordResponseList(_message.Message):
    __slots__ = ["inventoryRecord"]
    INVENTORYRECORD_FIELD_NUMBER: _ClassVar[int]
    inventoryRecord: _containers.RepeatedCompositeFieldContainer[InventoryRecord]
    def __init__(self, inventoryRecord: _Optional[_Iterable[_Union[InventoryRecord, _Mapping]]] = ...) -> None: ...

class InventoryAtPercentile(_message.Message):
    __slots__ = ["at_percentile"]
    AT_PERCENTILE_FIELD_NUMBER: _ClassVar[int]
    at_percentile: float
    def __init__(self, at_percentile: _Optional[float] = ...) -> None: ...

class InventoryRecord(_message.Message):
    __slots__ = ["id", "name", "description", "unitPrice", "quantityInStock", "inveneotryValue", "reorderLevel", "reorderTimeInDays", "quantityInReorder", "discontinued"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    UNITPRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITYINSTOCK_FIELD_NUMBER: _ClassVar[int]
    INVENEOTRYVALUE_FIELD_NUMBER: _ClassVar[int]
    REORDERLEVEL_FIELD_NUMBER: _ClassVar[int]
    REORDERTIMEINDAYS_FIELD_NUMBER: _ClassVar[int]
    QUANTITYINREORDER_FIELD_NUMBER: _ClassVar[int]
    DISCONTINUED_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    unitPrice: float
    quantityInStock: int
    inveneotryValue: float
    reorderLevel: int
    reorderTimeInDays: int
    quantityInReorder: int
    discontinued: bool
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., unitPrice: _Optional[float] = ..., quantityInStock: _Optional[int] = ..., inveneotryValue: _Optional[float] = ..., reorderLevel: _Optional[int] = ..., reorderTimeInDays: _Optional[int] = ..., quantityInReorder: _Optional[int] = ..., discontinued: bool = ...) -> None: ...
