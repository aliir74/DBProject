import datetime as t
from http.server import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep
import cgi






def getFormattedDate():
    formattedDate = ("" + str(t.datetime.now().year) + "-"
                           + str(t.datetime.now().month) + "_"
                           + str(t.datetime.now().day) + " "
                           + str(t.datetime.now().hour) + ":"
                           + str(t.datetime.now().minute) + ":"
                           + str(t.datetime.now().second) +"" )
    return formattedDate







class getInformation():
    user = "testuser"
    password = "test123test!"
    DB_NAME = "Test50"
    PORT = "3306"
    host = "localhost"

    def getUser(self):
        return (self.user)
    def getPassword(self):
        return (self.password)
    def getDB(self):
        return (self.DB_NAME)
    def getPort(self):
        return (self.PORT)
    def getHost(self):
        return (self.host)


