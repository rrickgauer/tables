from __future__ import annotations
from tables.utilities.printers import dump_json


class BaseCommand:
    
    def __str__(self) -> str:
        return dump_json(self.__dict__)