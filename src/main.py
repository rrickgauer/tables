from __future__ import annotations
from CliArgs import CliArgs
from ConfigData import ConfigData
from Controller import Controller
import constants

cliArgs = CliArgs()

if cliArgs.deleteConfigFile:
    ConfigData.deleteConfigFile()


controller = Controller(cliArgs.views, cliArgs.markdown)
controller.loadTables()
controller.printTables()

# save the output if the user wanted to
if cliArgs.save:
    controller.writeOutputToFile(constants.OUTPUT_FILE)
