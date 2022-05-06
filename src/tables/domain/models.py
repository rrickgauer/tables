"""
********************************************************************************************

Domain models

********************************************************************************************
"""

from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from .enums import SqlTableType, ViewCommandOutputFormat
from .views import SqlColumnDescription

@dataclass
class DatabaseConnection:
    """Database Connection"""
    
    name      : str      = None
    user      : str      = None
    host      : str      = None
    database  : str      = None
    password  : str      = None
    created_on: datetime = None


@dataclass
class ViewCommandCliArgFlags:
    """Optional cli flags for the view command."""

    name    : str                     = None
    all     : bool                    = False
    tables  : bool                    = False
    views   : bool                    = False
    columns : list[str]               = None
    output  : str                     = None
    format  : ViewCommandOutputFormat = ViewCommandOutputFormat.TABLE
    sort    : str                     = None



@dataclass
class TableDump:
    table_name : str                        = None
    table_type : SqlTableType               = None
    columns    : list[SqlColumnDescription] = None
