

from __future__ import annotations
from dataclasses import dataclass
from .enums import SqlTableType

@dataclass
class SqlTableTypeView:
    """View returned from SHOW FULL TABLES sql command."""

    table_name: str          = None
    table_type: SqlTableType = None


@dataclass
class SqlColumnDescription:
    
    ordinal_position         : int = None
    column_name              : str = None
    column_default           : str = None
    is_nullable              : str = None
    data_type                : str = None
    character_maximum_length : int = None
    character_octet_length   : int = None
    numeric_precision        : str = None
    numeric_scale            : str = None
    datetime_precision       : int = None
    character_set_name       : str = None
    collation_name           : str = None
    column_type              : str = None
    column_key               : str = None
    extra                    : str = None
    privileges               : str = None
    column_comment           : str = None
    generation_expression    : str = None
    srs_id                   : str = None