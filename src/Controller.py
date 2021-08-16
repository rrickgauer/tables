from ConfigData import ConfigData
from DbConnection import DbConnection
from Table import Table
from TableTypes import TableTypes

class Controller:

    def __init__(self, a_bShowViews: bool=True):
        self.configData = ConfigData()
        self.dbCon = DbConnection(self.configData)
        self.tables = []
        self.showViews = a_bShowViews
        
    
    def loadTables(self):
        self._loadTableNames()
        self._loadTableMetadata()
        
    def _loadTableNames(self):
        self.dbCon.connect()
        sql = 'SHOW FULL TABLES'

        if self.showViews:
            sql += " WHERE Table_Type = 'BASE TABLE'"

        self.dbCon.cursor.execute(sql)
        myResult = self.dbCon.cursor.fetchall()

        for tableInfo in myResult:
            tableObj = Table(tableInfo[0],  TableTypes.TABLE)

            if tableInfo[1] == TableTypes.VIEW.value:
                tableObj.tableType = TableTypes.VIEW
            
            self.tables.append(tableObj)
        
        self.dbCon.close()

    def _loadTableMetadata(self):
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
    
