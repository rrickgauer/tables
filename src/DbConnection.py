from ConfigData import ConfigData
# import mysql.connector
import mysql.connector
import mysql.connector.cursor


class DbConnection:

    def __init__(self, configData: ConfigData):
        self._configData = configData
        self._db = None
        self._cursor = None
    
    @property
    def configData(self) -> ConfigData:
        """Configuration data
        """
        return self._configData
    
    @configData.setter
    def configData(self, value):
        self._configData = value

    @property
    def db(self):
        """Database connection
        """
        return self._db

    @db.setter
    def db(self, value):
        self._db = value
    
    @property
    def cursor(self) -> mysql.connector.cursor:
        """Database cursor
        """
        return self._cursor

    @cursor.setter
    def cursor(self, value):
        self._cursor = value


    def connect(self):
        """Connect to the database.
        """
        configDataDict = self._configData.toDict()
        self.db = mysql.connector.connect(**configDataDict)
        self.cursor = self.db.cursor()

    
    def close(self):
        self.db.close()