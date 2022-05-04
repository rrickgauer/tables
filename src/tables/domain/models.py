"""
********************************************************************************************

Domain models

********************************************************************************************
"""

from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime

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

    all   : bool = False
    tables: bool = False
    views : bool = False



