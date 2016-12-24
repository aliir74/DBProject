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




def sensorFormattedData(text,type):

    if(type == "GasSensor"):
        formattedData = "Gas Sensor ID : " + str(text[0]) + " Owner : " + str(text[1]) + " Last Registered Time : " + str(text[3]) + " CO2 : " + str(text[4]) + " CO : " + str(text[5]) + " CH4 : " + str(text[6])
    if(type == "TempSensor"):
        formattedData = "Temperature Sensor ID : " + str(text[0]) + " Owner : " + str(text[1]) + " Last Registered Time : " + str(text[3]) + " Temperature : " + str(text[4])
    if(type == "HumiditySensor"):
        formattedData = "Humidity Sensor ID : " + str(text[0]) + " Owner : " + str(text[1]) + " Last Registered Time : " + str(text[3]) + " Air Humidity : " + str(text[4]) + " Soil Humidity : " + str(text[5])
    if(type == "LightSensor"):
        formattedData = "Light Sensor ID : " + str(text[0]) + " Owner : " +str(text[1]) + " Last Registered Time : " + str(text[3]) + " Light Intensity : " + str(text[4]) + " BLight Intensity : " + str(text[5])
    return formattedData






class getInformation():
    user = "testuser"
    password = "test123test!"
    DB_NAME = "Test111"
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








