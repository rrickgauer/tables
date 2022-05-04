from __future__ import annotations
from tables.domain import views
from .base import BaseCommand
from tables.utilities import serializers
from tables.utilities.serializers import serialize_dataclass
from tables import sql as sql_engine
from tables.utilities.printers import get_basic_dict_list
from tables.domain.models import TableDump
from tables.domain.maps import DatabaseDumpMap
from tables.domain.enums import SqlTableType

class ViewCommand(BaseCommand):
    """Execute a view command."""
    
    def __init__(self, database: str):
        self._database = database
        self._tables: list[views.SqlTableTypeView] = None

    def load_tables(self):
        """Fetch the tables list and start up the sql engine."""

        db_result = sql_engine.get_all_database_tables(self._database)
        
        if not db_result.successful:
            raise db_result.error
        
        table_dicts = db_result.data or []
        self._tables = [serializers.to_sql_database_tables_list_view(t) for t in table_dicts]   

    def dump_tables_list(self) -> list[views.SqlTableTypeView]:
        return self._tables

    def dump_all(self) -> DatabaseDumpMap:
        tables = [t for t in self._tables]
        return self._dump_tables(tables)

    def dump_tables(self):
        tables = [t for t in self._tables if t.table_type == SqlTableType.TABLE]
        return self._dump_tables(tables)
    
    def dump_views(self):
        tables = [t for t in self._tables if t.table_type == SqlTableType.VIEW]
        return self._dump_tables(tables)


    def _dump_tables(self, tables: list[views.SqlTableTypeView]) -> DatabaseDumpMap:
        result = {}
        
        for table in tables:
            columns = sql_engine.get_table_schema(self._database, table.table_name)

            table_dump = TableDump(
                table_name = table.table_name,
                table_type = table.table_type,
                columns    = [serialize_dataclass(c, views.SqlColumnDescription) for c in columns]
            )

            result[table.table_name] = table_dump

        return result