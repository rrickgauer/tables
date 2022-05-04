

from __future__ import annotations
from dataclasses import dataclass
from .enums import SqlTableType

@dataclass
class SqlTableTypeView:
    """View returned from SHOW FULL TABLES sql command."""

    table_name: str          = None
    table_type: SqlTableType = None