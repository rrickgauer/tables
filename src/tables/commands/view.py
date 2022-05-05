from __future__ import annotations
from .base import BaseCommand
from tables import sql as sql_engine
from tables.utilities.serializers import to_sql_database_tables_list_view
from tables.utilities.serializers import serialize_dataclass
from tables.domain.models import TableDump
from tables.domain.maps import DatabaseDumpMap
from tables.domain.enums import SqlTableType
from tables.domain.views import SqlTableTypeView
from tables.domain.views import SqlColumnDescription

class ViewCommand(BaseCommand):
    """Execute a view command."""
    
    def __init__(self, database: str):
        """View command.

        A view command fetches the datbase's table/view schemas.

        Args:
            database (str): Name of the database.
        """

        self._database = database
        self._tables: list[SqlTableTypeView] = None

    def load_tables(self):
        """Fetch and store the list of tables/views."""

        db_result = sql_engine.get_all_database_tables(self._database)
        
        if not db_result.successful:
            raise db_result.error
        
        table_dicts = db_result.data or []
        self._tables = [to_sql_database_tables_list_view(t) for t in table_dicts]   

    def dump_tables_list(self) -> list[SqlTableTypeView]:
        """Get a list of all the tables and views in the database."""
        return self._tables

    def dump_all(self) -> DatabaseDumpMap:
        """Dump table and view schemas."""
        tables = [t for t in self._tables]
        return self._dump_tables(tables)

    def dump_tables(self):
        """Dump table schemas."""
        tables = [t for t in self._tables if t.table_type == SqlTableType.TABLE]
        return self._dump_tables(tables)
    
    def dump_views(self):
        """Dump view schemas."""
        tables = [t for t in self._tables if t.table_type == SqlTableType.VIEW]
        return self._dump_tables(tables)


    def _dump_tables(self, tables: list[SqlTableTypeView]) -> DatabaseDumpMap:
        """Get the schemas of the specified list tables/views."""

        result = {}
        
        for table in tables:
            columns = sql_engine.get_table_schema(self._database, table.table_name)

            table_dump = TableDump(
                table_name = table.table_name,
                table_type = table.table_type,
                columns    = [serialize_dataclass(c, SqlColumnDescription) for c in columns]
            )

            result[table.table_name] = table_dump

        return result