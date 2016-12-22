import mysql.connector
import Initialization
import MainUpdator



#user = input("username: ")
#password = input("password: ")
user = 'testuser'
password = 'test123test!'

DB_NAME = "Test106"
PORT = "3306"
Initialization.create(DB_NAME , PORT)
u = MainUpdator.Updator(username=user, password=password, host='localhost', DB_NAME=DB_NAME, PORT=PORT)
u.incStock("gasSensor")
u.incStock("gasSensor")
u.decStock("gasSensor")
u.insert("User" , ("mxii1994" , "Mehdi" , "Safaee" , "mono1728"))
u.insert("User" , ("ali94" , "Ali" , "Irani" , "ali0241"))

print ("heh")