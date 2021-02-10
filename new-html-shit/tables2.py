import mysql.connector
import getpass
from os import path
import argparse
import webbrowser
import json
import pathlib
from Row import Row
from Table import Table

def createNewConfigFile():
    configFileUserInput = {
        "host"     : input('Host: '),
        "user"     : input('User: '),
        "database" : input('Database: '),
        "passwd"   : getpass.getpass(),
    }

    jsonString = json.dumps(configFileUserInput)
    with open(".tables-mysql-info.json", "w") as newConfigFile:
        newConfigFile.write(jsonString)

# return the data from the local .tables.config file
def getConfigData():
    with open('.tables-mysql-info.json') as configFile:
        configData = json.loads(configFile.read())
        return configData

#################################### MAIN #######################################


# create new config file if one does not exist in the local directory
if not path.exists('.tables-mysql-info.json'):
    createNewConfigFile()


# initialize the containers
output = [] 
tableNames = []


# connect to database
configData = getConfigData()
mydb = mysql.connector.connect(**configData)
mycursor = mydb.cursor()

# fetch all the tables from the database
sql = "SHOW FULL TABLES WHERE Table_type != 'VIEW'"

mycursor.execute(sql)
myResult = mycursor.fetchall()

for x in myResult: 
    tableNames.append(x[0])


# for every table in the list, retrieve it's field list using the describe command
tableList = []

# load up the python objects
for tableName in tableNames:
    # make new table object with the name of the table
    table = Table(tableName)

    # fetch all the column data for the table
    sql = "describe " + table.name
    mycursor.execute(sql)
    myResult = mycursor.fetchall()

    # add each column data row to the table
    for x in myResult:
        table.addRow(x)

    # add the table to the list of tables
    tableList.append(table)


tableDictsList = []

# convert each table object into a dict and 
# add it to the list of table dicts
for table in tableList:
    tableDictsList.append(table.getDictVersion())

# generate a javascript file to hold the data
jsonString = json.dumps(tableDictsList, indent=4)
jsFileContent = "const G_TABLE_DATA = " + jsonString + ";"


with open("html/JS-RAW-TABLE-DATA.js", "w") as jsOutputFile:
    jsOutputFile.write(jsFileContent)

# open the html file
currentPath = str(pathlib.Path(__file__).parent.absolute()) + "\\"
htmlFile = currentPath + "html\\index.html"
webbrowser.open(htmlFile, new=2)

