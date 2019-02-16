import requests

class FhemConnector:
    __instance = None
    _fhemDomain = 'http://10.13.200.5:8083/fhem'

    @staticmethod
    def getInstance():
        if FhemConnector.__instance == None:
            FhemConnector()
        return FhemConnector.__instance 

    def __init__(self):
        if FhemConnector.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            FhemConnector.__instance = self

    def executeFhemCommand(self, command, brackets = True):
        parameters = ''
        if(brackets):
            parameters = "?cmd={{{0}}}"
        else:
            parameters = "?cmd={0}"
        
        url = self._fhemDomain + (parameters + "&XHR=1").format(command)
        return requests.get(url).text