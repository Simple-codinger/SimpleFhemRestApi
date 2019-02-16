import requests
from FhemConnector import FhemConnector

def rooms_get():
    command = 'roomsList(1)'
    rooms = FhemConnector.getInstance().executeFhemCommand(command)
    return rooms.splitlines()

def devices_get(room):
    command = ('list%20room={0}').format(room)
    devices = FhemConnector.getInstance().executeFhemCommand(command, False)
    return devices.splitlines()