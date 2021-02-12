from Row import Row

class Table:

    def __init__(self, name):
        self.name = name
        self.rows = []
    
    def addRow(self, newRow):
        self.rows.append(Row(newRow))

    def getDictVersion(self):
        rowsDictList = self.getRowsDictList()

        output = {
            "table": self.name,
            "data": rowsDictList
        }

        return output


    def getRowsDictList(self):
        rowsDictList = []

        for row in self.rows:
            rowsDictList.append(row.getDict())

        return rowsDictList