import os
import Utilities as Util
import getpass

class ConfigData:
    
    # static properties
    CONFIG_FILE = '.tables-mysql-info.json'

    def __init__(self):
        """MySQL configuration file class.
        """
        self._user = None
        self._host = None
        self._database = None
        self._passwd = None
        
        self.readConfigData()
    
    @property
    def user(self) -> str:
        """Username
        """
        return self._user

    
    @property
    def host(self) -> str:
        """Host or IP addess
        """
        return self._host

    
    @property
    def database(self) -> str:
        """Database name
        """
        return self._database

    
    @property
    def passwd(self) -> str:
        """Password
        """        
        return self._passwd

    
    def readConfigData(self):
        """Read in the config file.
        If one does not exist, create a new one.
        """
        
        # create a new config file if it doesn't exist
        if not self.doesConfigFileExist():
            self.createNewConfigFile()
        
        # read in the file
        configFileDict = Util.readJsonDataFromFile(ConfigData.CONFIG_FILE)
        
        # set the appropriate data members
        self._user     = configFileDict.get('user')
        self._host     = configFileDict.get('host')
        self._database = configFileDict.get('database')
        self._passwd   = configFileDict.get('passwd')
        

    def doesConfigFileExist(self) -> bool:
        """Checks if the config file already exists.

        Returns:
            bool: true means config file exists, otherwise false.
        """
        return os.path.exists(ConfigData.CONFIG_FILE)


    def createNewConfigFile(self):
        """Create a new config file.
        """
        self._user     = input('user: ')
        self._host     = input('host: ')
        self._database = input('database: ')
        self._passwd   = getpass.getpass('passwd: ')
        
        configDict = self.toDict()
        Util.writeDictToFile(configDict, ConfigData.CONFIG_FILE)


    def toDict(self) -> dict:
        """Transform the object into a dict.
        """
        resultDict = dict(user=self.user, host=self.host, database=self.database, passwd=self.passwd)
        return resultDict
    
    @staticmethod
    def deleteConfigFile():
        """Delete the current config file
        """
        os.remove(ConfigData.CONFIG_FILE)
