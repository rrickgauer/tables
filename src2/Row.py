class Row:

    def __init__(self, rowStruct):
        self.setMembers(rowStruct)


    def setMembers(self, rowStruct):
        self.field   = rowStruct[0]
        self.type    = rowStruct[1]
        self.null    = rowStruct[2]
        self.key     = rowStruct[3]
        self.default = rowStruct[4]
        self.extra   = rowStruct[5]


    def getDict(self):
        return self.__dict__