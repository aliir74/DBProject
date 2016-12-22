import mysql.connector
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
            self.cursor.execute(insertionData, tableData)
            self.cnx.commit()
        if(tableName=="Product"):
            insertionData = ("INSERT INTO " + tableName +
                   "(productCode, productType, price, stock)"
                   "VALUES (%s, %s, %s, %s)")
            self.cursor.execute(insertionData, tableData)
            self.cnx.commit()
        if(tableName=="GasSensor"):
            insertionData = ("INSERT INTO " + tableName +
                   "(productID , username , productCode , time , CO2 , CO , CH4)"
                   "VALUES (%s, %s, %s, %s , %s , %s , %s)")
            self.cursor.execute(insertionData, tableData)
            self.cnx.commit()
        if(tableName=="TempSensor"):
            print("inserting")
            insertionData = ("INSERT INTO " + tableName +
                   " (productID , username , productCode , time , temperature)"
                   "VALUES (%s, %s , %s , %s , %s)")
            self.cursor.execute(insertionData, tableData)
            self.cnx.commit()
        if(tableName=="HumiditySensor"):
            insertionData = ("INSERT INTO " + tableName +
                   "(productID , username , productCode , time , aurHumidity , soilHumidity)"
                   "VALUES (%s, %s, %s, %s , %s , %s)")
            self.cursor.execute(insertionData, tableData)
            self.cnx.commit()
        if(tableName=="LightSensor"):
            insertionData = ("INSERT INTO " + tableName +
                   "(productID , username , productCode , time , lightIntensity , bLightIntensity)"
                   "VALUES (%s, %s, %s, %s , %s , %s)")
            self.cursor.execute(insertionData, tableData)
            self.cnx.commit()

        self.cursor.close()
        self.cnx.close()
        return ()





    def incStock(self, product):
        self.cnx = mysql.connector.connect(user=self.username , password=self.password , host=self.host , database=self.DB_NAME , port=self.PORT  )
        self.cursor = self.cnx.cursor()
        self.cursor.execute("UPDATE Product SET stock=stock+1 WHERE productType=" +product)
        self.cnx.commit()
        self.cursor.close()
        self.cnx.close()
        return ()

    def decStock(self, product):
        if (self.getStock(product)):
            self.cnx = mysql.connector.connect(user=self.username , password=self.password , host=self.host , database=self.DB_NAME , port=self.PORT  )
            self.cursor = self.cnx.cursor()
            self.cursor.execute("UPDATE Product SET stock=stock-1  WHERE stock>0 and productType=" +product)
            self.cnx.commit()
        self.cursor.close()
        self.cnx.close()
        return ()

    def getStock(self,product):
        self.cnx = mysql.connector.connect(user=self.username , password=self.password , host=self.host , database=self.DB_NAME , port=self.PORT  )
        self.cursor = self.cnx.cursor()
        self.cursor.execute("SELECT stock FROM Product WHERE productType=" +product)
        stockTuple = (self.cursor.fetchall()[0])
        self.cursor.close()
        self.cnx.close()
        return (stockTuple[0])


    def getDevices(self,username):
        self.cnx = mysql.connector.connect(user=self.username , password=self.password , host=self.host , database=self.DB_NAME , port=self.PORT  )
        self.cursor = self.cnx.cursor()
        self.cursor.execute("SELECT * FROM gasSensor WHERE username=" +username)
        gasSensors = (self.cursor.fetchall())
        self.cursor.execute("SELECT * FROM tempSensor WHERE username=" +username)
        tempSensors = (self.cursor.fetchall())
        self.cursor.execute("SELECT * FROM humiditySensor WHERE username=" +username)
        humiditySensors = (self.cursor.fetchall())
        self.cursor.execute("SELECT * FROM lightSensor WHERE username=" +username)
        lightSensors = (self.cursor.fetchall())
        self.cursor.close()
        self.cnx.close()
        devices = [gasSensors,tempSensors,humiditySensors,lightSensors]
        return (devices)


'''
    def sellDevices(self,product,username):
        if (self.getStock(product)):

            self.cursor.execute(insertionData, tableData)
            self.cnx.commit()


'''







