from CliArgs import CliArgs
from ConfigData import ConfigData

cliArgs = CliArgs()

if cliArgs.deleteConfigFile:
    ConfigData.deleteConfigFile()


configData = ConfigData()










