import mysql.connector
import Initialization
import MainUpdator



user = 'testuser'
password = 'test123test!'


DB_NAME = "Test152"
PORT = "3306"
Initialization.create(DB_NAME , PORT)


u = MainUpdator.Updator(username=user, password=password, host='localhost', DB_NAME=DB_NAME, PORT=PORT)



print ("heh")