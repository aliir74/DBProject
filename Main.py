import mysql.connector
import Initialization
import MainUpdator
DB_NAME = "Test64"
PORT = "4800"
Initialization.create(DB_NAME , PORT)
u = MainUpdator.Updator('mxii1994','mono1728','localhost',DB_NAME,PORT)
u.incStock("'gasSensor'")
u.incStock("'gasSensor'")
u.decStock("'gasSensor'")
u.insert("User" , ("mxii1994" , "Mehdi" , "Safaee" , "mono1728"))
u.insert("User" , ("ali94" , "Ali" , "Irani" , "ali0241"))

print ("heh")