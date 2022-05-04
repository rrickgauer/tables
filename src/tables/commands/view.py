from __future__ import annotations
from tables.domain import views
from .base import BaseCommand
from tables.utilities import serializers
from tables import sql as sql_engine

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

    def dump_tables_list(self):
        print('dump table list')


    def dump_all(self):
        print('dump all')

    def dump_tables(self):
        print('dump tables')
    
    def dump_views(self):
        print('dump views')