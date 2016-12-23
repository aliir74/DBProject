import mysql.connector
import Initialization
import MainUpdator
import GUI
from Utilities import getInformation as info



Initialization.create(info.getDB(info),info.getPort(info))


GUI.window()


print ("heh")