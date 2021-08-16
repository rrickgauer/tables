from CliArgs import CliArgs
from ConfigData import ConfigData
from DbConnection import DbConnection

cliArgs = CliArgs()

if cliArgs.deleteConfigFile:
    ConfigData.deleteConfigFile()


configData = ConfigData()


dbCon = DbConnection(configData)
dbCon.connect()


sql = 'SHOW FULL TABLES'

dbCon.cursor.execute(sql)
myResult = dbCon.cursor.fetchall()

for x in myResult:
    print(x)









