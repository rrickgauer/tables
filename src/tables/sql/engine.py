from __future__ import annotations
import pymysql.commands as db
from . import statements as sql_stmts




def get_all_database_tables(database):
    return db.selectAll(sql_stmts.GET_ALL_DATABASE_TABLES, (database,))


def get_table_schema(table):
    pass