import json

def writeDictToFile(a_dict: dict, a_strOutputFileName: str):
    """Write a python dictionary to a json file.

    Args:
        a_dict (dict): [description]
        a_strOutputFileName (str): [description]
    """

    # convert dict to json string
    jsonString = json.dumps(a_dict, indent=4)
    
    # write the string to the given output file
    outFile = open(a_strOutputFileName, 'w')
    outFile.write(jsonString)
    outFile.close()


def readJsonDataFromFile(a_strInputFileName: str) -> dict:
    """Read in a json file.

    Args:
        a_strInputFileName (str): Name of the file.

    Returns:
        dict: resulting dictionary.
    """

    inFile = open(a_strInputFileName) 
    resultDict = json.loads(inFile.read())
    inFile.close()

    return resultDict



