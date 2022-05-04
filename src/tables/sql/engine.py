from __future__ import annotations
import pymysql.credentials
import pymysql.commands as db
from . import statements as sql_stmts



class SqlEngine:

    def __init__(self, user=None, password=None, database=None, host=None):
        self._user     = user
        self._password = password
        self._database = database
        self._host     = host

    def start(self):
        pymysql.credentials.USER     = self._user
        pymysql.credentials.PASSWORD = self._password
        pymysql.credentials.DATABASE = self._database
        pymysql.credentials.HOST     = self._host

    
    def get_all_database_tables(self):
        return db.selectAll(sql_stmts.GET_ALL_DATABASE_TABLES, (self._database,))