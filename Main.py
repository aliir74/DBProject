import mysql.connector
import Initialization
import MainUpdator



user = 'testuser'
password = 'test123test!'


DB_NAME = "Test136"
PORT = "3306"
Initialization.create(DB_NAME , PORT)


u = MainUpdator.Updator(username=user, password=password, host='localhost', DB_NAME=DB_NAME, PORT=PORT)
u.insert("User" , ("mxii1994" , "Mehdi" , "Safaee" , "mono1728"))
u.insert("User" , ("ali94" , "Ali" , "Irani" , "ali0241"))
u.incStock("GasSensor")
u.incStock("GasSensor")
u.decStock("GasSensor")
u.sellDevices("mxii1994" , "GasSensor")
u.setStock("TempSensor" , "50")
u.sellDevices("mxii1994" , "TempSensor")
u.getSensorData("mxii1994")


print ("heh")