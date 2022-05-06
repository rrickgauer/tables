from __future__ import annotations
from tables.utilities.prettytables import dump_json


class BaseSchema:
    
    def __str__(self) -> str:
        return dump_json(self.__dict__)