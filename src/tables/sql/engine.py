from __future__ import annotations
import pymysql.commands as db
from . import statements as sql_stmts


class SqlEngine:

    def get_all_database_tables(self, database):
        return db.selectAll(sql_stmts.GET_ALL_DATABASE_TABLES, (database,))