from __future__ import annotations
from ConfigData import ConfigData
from DbConnection import DbConnection
from Table import Table
from TableTypes import TableTypes

class Controller:

    def __init__(self, showViews: bool=True, formatAsMarkdown: bool=False):
        """Controller class constructor

        Args:
            showViews (bool, optional): Include the views in the output. Defaults to True.
            formatAsMarkdown (bool, optional): Format output as markdown? Defaults to False.
        """
        self.configData: ConfigData = ConfigData()
        self.dbCon: DbConnection = DbConnection(self.configData)
        self.tables: list[Table] = []
        self.showViews = showViews
        self.formatAsMarkdown = formatAsMarkdown
        
    
    def loadTables(self):
        """Load the tables data"""
        self._loadTableNames()
        self._loadAllTableMetadata()
        
    def _loadTableNames(self):
        """Load the list of table names that are in the database"""

        # generate the sql statement
        sql = self._getShowTablesSqlStatement()

        # connect to the database and retrieve the tables recordset
        self.dbCon.connect()
        self.dbCon.cursor.execute(sql)
        dbResultRecords = self.dbCon.cursor.fetchall()

        # process each table record returned from the database
        # add the table objects to the list of table objects
        for tableRecord in dbResultRecords:
            tableObj = Table(tableRecord[0], TableTypes.TABLE, self.formatAsMarkdown)

            # determine the table type
            if tableRecord[1] == TableTypes.VIEW.value:
                tableObj.tableType = TableTypes.VIEW
            
            self.tables.append(tableObj)
        
        # close the connection
        self.dbCon.close()

    def _getShowTablesSqlStatement(self) -> str:
        """Get the sql statement for selecting the list of table names.

        Returns:
            str: SQL statement
        """
        sql = 'SHOW FULL TABLES'

        if self.showViews:
            sql += " WHERE Table_Type = 'BASE TABLE'"

        return sql

    def _loadAllTableMetadata(self):
        """Fetch each table's metadata."""
        self.dbCon.connect()

        for tableObj in self.tables:
            tableObj.loadMetadata(self.dbCon)
        
        self.dbCon.close()

    
    def printTables(self):
        print(self.getTablesOutput())
    
    def writeOutputToFile(self, a_strOutputFile: str):
        with open(a_strOutputFile, 'w') as outFile:
            outFile.write(self.getTablesOutput())


    def getTablesOutput(self) -> str:
        output = ''
        
        for tableObj in self.tables:
            output += tableObj.getPrettyTable()
            output += "\n\n\n"
            
        return output
    
