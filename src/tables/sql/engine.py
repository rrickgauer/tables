from __future__ import annotations
import pymysql.commands as db
from pymysql.structs import DbOperationResult
from . import statements as sql_stmts




def get_all_database_tables(database):
    return db.selectAll(sql_stmts.GET_ALL_DATABASE_TABLES, (database,))


def get_table_schema(database, table) -> list[dict]:
    parms = (
        database,
        table,
    )

    result = db.selectAll(sql_stmts.GET_TABLE_COLUMNS_INFO, parms)

    if not result.successful:
        raise result.error
    
    return result.data or []