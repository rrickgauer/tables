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

    user      : str      = None
    host      : str      = None
    database  : str      = None
    password  : str      = None
    name      : str      = None
    created_on: datetime = None
