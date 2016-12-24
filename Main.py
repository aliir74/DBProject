import mysql.connector
import _thread
import Initialization
import MainUpdator
from Utilities import getInformation as info

Initialization.create(info.getDB(info),info.getPort(info))

import Server

Server.runThread()

import GUI


print ("heh")