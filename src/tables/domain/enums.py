"""
********************************************************************************************

Domain model enums

********************************************************************************************
"""

from __future__ import annotations
from enum import Enum

class ExtendedEnum(Enum):
    """Customized extended enumerations"""

    @classmethod
    def values(cls) -> list:
        """Get a list of all the enum class values"""
        return list(map(lambda c: c.value, cls))

    @classmethod
    def names(cls) -> list[str]:
        """Get a list of all the enum class names"""
        return list(map(lambda c: c.name, cls))

    
    @classmethod
    def getByKey(cls, key: str) -> Enum | None:
        """Get the enum value that has the specified key"""
        return cls._member_map_.get(key)



class CliCommands(ExtendedEnum):
    """CLI commands"""

    LIST   = 'list'
    ADD    = 'add'
    VIEW   = 'view'
    DELETE = 'delete'



class SqlTableType(ExtendedEnum):
    """MySQL Table Types"""

    TABLE = 'BASE TABLE'
    VIEW = 'VIEW'


class ViewCommandOutputFormat(str, ExtendedEnum):
    TABLE    = 'table'
    MARKDOWN = 'markdown'
    HTML     = 'html'
    JSON     = 'json'