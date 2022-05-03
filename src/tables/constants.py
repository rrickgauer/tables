from __future__ import annotations
from enum import Enum
import os
import tables

class Paths:
    CWD = os.getcwd()
    EXE = os.path.dirname(tables.__file__)


class TablesEnum(Enum):
    pass


class Files(str, TablesEnum):
    CONNECTIONS = '.tables-connections.json'


def getAbs(file: TablesEnum) -> str:
    return os.path.join(Paths.EXE, file.value)
