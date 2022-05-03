from __future__ import annotations
from TableTypes import TableTypes
from Row import Row
from prettytable import PrettyTable
from DbConnection import DbConnection


class Table:

    def __init__(self, name: str, tableType: TableTypes=TableTypes.TABLE):
        self._name = name
        self._tableType = tableType
        self._rows = []

    @property
    def name(self) -> str:
        """Name of the table
        """
        return self._name
    
    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def tableType(self) -> TableTypes:
        """Type of table (base table or view)
        """
        return self._tableType
    
    @tableType.setter
    def tableType(self, value: TableTypes):
        self._tableType = value

    @property
    def rows(self) -> list[Row]:
        """Rows in the table (it's metadata).
        """
        return self._rows

    @rows.setter
    def rows(self, value):
        """Set the rows of the table oject

        Args:
            value (list[tuple]): list of MySQL metadata tuples that make up the rows.
        """
        self._rows.clear()

        for rowTuple in value:
            self.addRow(rowTuple)


    def addRow(self, rowStruct: tuple):
        rowObj = Row(rowStruct)
        self._rows.append(rowObj)

    def toDict(self) -> dict:
        """Transform the object to a dict
        """
        outDict = dict(name=self.name, tableType=self.tableType, rows=self.rowsToDict())

        return outDict

    def rowsToDict(self) -> dict:
        """Get a transformed list of rows objects to a list row object dictionaries.
        """
        resultDict = []

        for row in self.rows:
            resultDict.append(row.toDict())
        
        return resultDict

    
    def printTable(self):
        outText = self.getPrettyTable()
        print(outText)


    def getPrettyTable(self) -> str:
        prettyTable = PrettyTable(Row.FIELD_NAMES_LIST)
        prettyTable.align = "l"
        
        for row in self.rows:
            prettyTable.add_row(row.toList())
        
        displayName = self.name

        if self.tableType == TableTypes.VIEW:
            displayName = f'''{self.name} (VIEW)'''

        outText = f'''{displayName}:\n{prettyTable.get_string()}'''

        return outText

    
    def loadMetadata(self, dbCon: DbConnection):
        sql = f'''DESCRIBE {self.name}'''
        dbCon.cursor.execute(sql)
        self.rows = dbCon.cursor.fetchall()



            
