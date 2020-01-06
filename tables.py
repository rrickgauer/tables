import mysql.connector
import getpass
import os.path
from os import path
import argparse

def createNewConfigFile():
    configFileUserInput = {
        "user"     : input('User: '),
        "host"     : input('Host: '),
        "database" : input('Database: '),
        "passwd"   : getpass.getpass(),
    }

    # write data to the config file
    newConfigFile = open(".tables.config", "w")
    newConfigFile.write(configFileUserInput['user'] + "\n")
    newConfigFile.write(configFileUserInput['host'] + "\n")
    newConfigFile.write(configFileUserInput['database'] + "\n")
    newConfigFile.write(configFileUserInput['passwd'] + "\n")
    newConfigFile.close()

# return the data from the local .tables.config file
def getConfigData():
    with open('.tables.config') as f:
        lines = list(f)

        configData = {
            "user" : lines[0],
            "host" : lines[1],
            "database" : lines[2],
            "passwd" : lines[3].strip()
        }
        return configData

def getTableRow(row):
    dict = {
        "field"   : row[0],
        "type"    : row[1],
        "null"    : row[2],
        "key"     : row[3],
        "default" : row[4],
        "extra"   : row[5]
    }
    return dict

def processData(queryData):
    rows = []
    for row in queryData:
        rows.append(getTableRow(row))
    return rows

def printHeader(tableName):

    print('\n\n' + tableName + ':')
    printDottedLine()
    printLine("Field", "Type")
    printDottedLine()

def printLine(field, type):
    print(f'| {field:40} | {type:60} |')

def printDottedLine():
    dashes1 = '-' * 42
    dashes2 = '-' * 62
    print('+' + dashes1 + '+' + dashes2 + '+')


#################################### MAIN #######################################

# assign command line arguments
parser = argparse.ArgumentParser(description="View your database table's fields and types")
parser.add_argument('-t', '--tables', nargs="+", help="list of tables you want displayed")
args = parser.parse_args()

# create new config file if one does not exist in the local directory
if not path.exists('.tables.config'):
    createNewConfigFile()

# get the config file data
configData = getConfigData()
mydb = mysql.connector.connect(**configData)
mycursor = mydb.cursor()

# clear the screen
print("\n" * 200)

# if no table arguments print list of all tables
if args.tables == None:
    sql = "show tables"
    mycursor.execute(sql)
    myResult = mycursor.fetchall()
    for x in myResult:
        print(x[0])

# print schema of all tables listed in the arguments
else:
    for table in args.tables:
        sql = "describe " + table
        mycursor.execute(sql)
        myResult = mycursor.fetchall()

        rows = processData(myResult)

        printHeader(table)
        for row in rows:
            printLine(row["field"], row["type"])
        printDottedLine()
