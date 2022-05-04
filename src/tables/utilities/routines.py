from __future__ import annotations
from tables.domain import models
import pymysql.credentials

def set_pymysql_credentials(database_connection: models.DatabaseConnection):
    pymysql.credentials.USER     = database_connection.user
    pymysql.credentials.PASSWORD = database_connection.password
    pymysql.credentials.DATABASE = database_connection.database
    pymysql.credentials.HOST     = database_connection.host