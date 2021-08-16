from __future__ import annotations

class Row:

    # static properties
    COL_NAME_FIELD   = 'Field'
    COL_NAME_TYPE    = 'Type'
    COL_NAME_NULL    = 'Null'
    COL_NAME_KEY     = 'Key'
    COL_NAME_DEFAULT = 'Default'
    COL_NAME_EXTRA   = 'Extra'

    FIELD_NAMES_LIST = [COL_NAME_FIELD, COL_NAME_TYPE, COL_NAME_NULL, COL_NAME_KEY, COL_NAME_DEFAULT, COL_NAME_EXTRA]

    def __init__(self, rowStruct):
        self.setMembers(rowStruct)

    def setMembers(self, rowStruct):
        self._field   = rowStruct[0]
        self._type    = rowStruct[1]
        self._null    = rowStruct[2]
        self._key     = rowStruct[3]
        self._default = rowStruct[4]
        self._extra   = rowStruct[5]

    @property
    def field(self) -> str:
        return self._field

    @field.setter
    def field(self, value: str):
        self._field = value

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str):
        self._type = value

    @property
    def null(self) -> str:
        return self._null

    @null.setter
    def null(self, value: str):
        self._null = value

    @property
    def key(self) -> str:
        return self._key
    
    @key.setter
    def key(self, value: str):
        self._key = value

    @property
    def default(self) -> str:
        return self._default

    @default.setter
    def default(self, value: str):
        self._default = value

    @property
    def extra(self) -> str:
        return self._extra

    @extra.setter
    def extra(self, value: str):
        self._extra = value
    
    def toList(self) -> list[str]:
        outList = list(self.toDict().values())
        return outList

    def toDict(self) -> dict:
        outDict = dict()
        
        outDict[Row.COL_NAME_FIELD]   = self.field
        outDict[Row.COL_NAME_TYPE]    = self.type
        outDict[Row.COL_NAME_NULL]    = self.null
        outDict[Row.COL_NAME_KEY]     = self.key
        outDict[Row.COL_NAME_DEFAULT] = self.default
        outDict[Row.COL_NAME_EXTRA]   = self.extra

        return outDict

