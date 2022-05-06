from __future__ import annotations
from enum import Enum
import os
import tables

SQL_DATA_ENCODING = 'utf-8'

class Paths:
    CWD = os.getcwd()
    EXE = os.path.dirname(tables.__file__)


class TablesEnum(Enum):
    pass


class Files(str, TablesEnum):
    DIRECTORY = 'data-files'
    CONNECTIONS = '.tables-database_connections.json'


def getAbs(file: TablesEnum) -> str:
    return os.path.join(Paths.EXE, Files.DIRECTORY.value, file.value)
