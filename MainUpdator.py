import mysql.connector
import datetime as t
from mysql.connector import errorcode


class Updator :

    def __init__(self, username , password , host  , DB_NAME , PORT):
        self.username = username
        self.password = password
        self.host = host
        self.DB_NAME = DB_NAME
        self.PORT = PORT




    def insert(self, tableName , tableData):
        self.cnx = mysql.connector.connect(user=self.username , password=self.password , host=self.host , database=self.DB_NAME , port=self.PORT  )
        self.cursor = self.cnx.cursor()
        if(tableName=="User"):
            print('inserting')
            insertionData = ("INSERT INTO " + tableName +
                   "(username, name, family, password)"
                   "VALUES (%s, %s, %s, %s)")
        elif(tableName=="Product"):
            insertionData = ("INSERT INTO " + tableName +
                   "(productCode, productType, price, stock)"
                   "VALUES (%s, %s, %s, %s)")
        elif(tableName=="GasSensor"):
            insertionData = ("INSERT INTO " + tableName +
                   "(productID , username , productCode , time , CO2 , CO , CH4)"
                   "VALUES (%s, %s, %s, %s , %s , %s , %s)")
        elif(tableName=="TempSensor"):
            print("inserting")
            insertionData = ("INSERT INTO " + tableName +
                   " (productID , username , productCode , time , temperature)"
                   "VALUES (%s, %s , %s , %s , %s)")
        elif(tableName=="HumiditySensor"):
            insertionData = ("INSERT INTO " + tableName +
                   "(productID , username , productCode , time , aurHumidity , soilHumidity)"
                   "VALUES (%s, %s, %s, %s , %s , %s)")
        elif(tableName=="LightSensor"):
            insertionData = ("INSERT INTO " + tableName +
                   "(productID , username , productCode , time , lightIntensity , bLightIntensity)"
                   "VALUES (%s, %s, %s, %s , %s , %s)")
        else:
            print("TableName is unknown!")
        self.cursor.execute(insertionData, tableData)
        self.cnx.commit()


        self.cursor.close()
        self.cnx.close()



    def insertRaw(self, username , product):
        insertionData = ("INSERT INTO " + product +
                   "(username , productCode , time)"
                   "VALUES (%s ,%s ,%s)")

        formattedDate = ("" + str(t.datetime.now().year) + "-"
                           + str(t.datetime.now().month) + "_"
                           + str(t.datetime.now().day) + " "
                           + str(t.datetime.now().hour) + ":"
                           + str(t.datetime.now().minute) + ":"
                           + str(t.datetime.now().second) +"" )

        tableData = (username,self.getProductCode(product),formattedDate)
        self.cnx = mysql.connector.connect(user=self.username , password=self.password , host=self.host , database=self.DB_NAME , port=self.PORT  )
        self.cursor = self.cnx.cursor()
        self.cursor.execute(insertionData, tableData)
        self.cnx.commit()
        self.cursor.close()
        self.cnx.close()






    def incStock(self, product):
        self.cnx = mysql.connector.connect(user=self.username , password=self.password , host=self.host , database=self.DB_NAME , port=self.PORT  )
        self.cursor = self.cnx.cursor()
        self.cursor.execute("""UPDATE Product SET stock=stock+1 WHERE productType= %s""" , (product,))
        self.cnx.commit()
        self.cursor.close()
        self.cnx.close()

    def decStock(self, product):
        if (self.getStock(product)):
            self.cnx = mysql.connector.connect(user=self.username , password=self.password , host=self.host , database=self.DB_NAME , port=self.PORT  )
            self.cursor = self.cnx.cursor()
            self.cursor.execute("""UPDATE Product SET stock=stock-1 WHERE productType=%s""" , (product,))
            self.cnx.commit()
        self.cursor.close()
        self.cnx.close()

    def getStock(self,product):
        self.cnx = mysql.connector.connect(user=self.username , password=self.password , host=self.host , database=self.DB_NAME , port=self.PORT  )
        self.cursor = self.cnx.cursor()
        self.cursor.execute("""SELECT stock FROM Product WHERE productType= %s""" , (product,))
        stockTuple = (self.cursor.fetchall()[0])
        self.cursor.close()
        self.cnx.close()
        return (stockTuple[0])


    def setStock(self,product,amount):
        self.cnx = mysql.connector.connect(user=self.username , password=self.password , host=self.host , database=self.DB_NAME , port=self.PORT  )
        self.cursor = self.cnx.cursor()
        self.cursor.execute("""UPDATE Product SET stock = %s WHERE productType= %s""" , (amount , product))
        self.cnx.commit()
        self.cursor.close()
        self.cnx.close()


    def getDevices(self,username):
        self.cnx = mysql.connector.connect(user=self.username , password=self.password , host=self.host , database=self.DB_NAME , port=self.PORT  )
        self.cursor = self.cnx.cursor()
        self.cursor.execute("""SELECT * FROM GasSensor WHERE username=%s""" ,(username,))
        gasSensors = (self.cursor.fetchall())
        self.cursor.execute("""SELECT * FROM TempSensor WHERE username=%s""" ,(username,))
        tempSensors = (self.cursor.fetchall())
        self.cursor.execute("""SELECT * FROM HumiditySensor WHERE username=%s""" ,(username,))
        humiditySensors = (self.cursor.fetchall())
        self.cursor.execute("""SELECT * FROM LightSensor WHERE username=%s""" ,(username,))
        lightSensors = (self.cursor.fetchall())
        self.cursor.close()
        self.cnx.close()
        devices = [gasSensors,tempSensors,humiditySensors,lightSensors]
        return (devices)



    def sellDevices(self,username,product):
        if (self.getStock(product)):
            self.decStock(product)
            self.insertRaw(username,product)
        else:
            print("we're out of " + product)





    def getProductCode(self,product):
        self.cnx = mysql.connector.connect(user=self.username , password=self.password , host=self.host , database=self.DB_NAME , port=self.PORT  )
        self.cursor = self.cnx.cursor()
        self.cursor.execute("""SELECT productCode FROM Product WHERE productType=%s""" , (product,))
        productCodeTuple = (self.cursor.fetchall()[0])
        self.cursor.close()
        self.cnx.close()
        return (productCodeTuple[0])



    def getSensorData(self,username,):
        devices = self.getDevices(username)
        print(devices[0])
        print(devices[1])
        print(devices[2])
        print(devices[3])
