from __future__ import annotations
from tables.domain import models, views
from .base_command import BaseCommand
from tables import printers
from tables import serializers
from tables.sql import SqlEngine


class ViewCommand(BaseCommand):
    """Execute a view command."""
    
    def __init__(self, connection: models.DatabaseConnection):
        self._connection = connection
        self._sql_engine: SqlEngine = None
        self._tables: list[views.SqlTableTypeView] = None


    def load_tables(self):
        """Fetch the tables list and start up the sql engine."""
        self._setup_engine()
        self._fetch_tables_list()

    def _setup_engine(self):
        """Start up the sql engine"""
        self._sql_engine = SqlEngine(
            user     = self._connection.user,
            password = self._connection.password,
            database = self._connection.database,
            host     = self._connection.host,
        )

        self._sql_engine.start()

    def _fetch_tables_list(self):
        """Fetch a list of all the database's tables and their type."""

        db_result = self._sql_engine.get_all_database_tables()
        if not db_result.successful:
            raise db_result.error
        
        table_dicts = db_result.data or []
        self._tables = [serializers.to_sql_database_tables_list_view(t) for t in table_dicts]