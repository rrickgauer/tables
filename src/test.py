from CliArgs import CliArgs
from ConfigData import ConfigData

from Controller import Controller

cliArgs = CliArgs()

if cliArgs.deleteConfigFile:
    ConfigData.deleteConfigFile()


controller = Controller(cliArgs.views)
controller.loadTables()
controller.printTables()
if cliArgs.save:
    controller.writeOutputToFile('tables.output.txt')
    






