from __future__ import annotations


class TablesException(Exception):
    pass


class PrintersErrors:
    PRINT_OBJECTS_ARG_NULL = TablesException("data argument is None")
    PRINT_OBJECTS_ARG_NOT_LIST = TablesException("data argument is not a list")

