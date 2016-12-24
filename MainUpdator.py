import mysql.connector
import Utilities
from Utilities import getInformation as info


class Updator :

    def __init__(self):
        self.username = info.getUser(info)
        self.password = info.getPassword(info)
        self.host = info.getHost(info)
        self.DB_NAME = info.getDB(info)
        self.PORT = info.getPort(info)




    def insert(self, tableName , tableData):
        self.cnx = mysql.connector.connect(user=self.username , password=self.password , host=self.host , database=self.DB_NAME , port=self.PORT  )
        self.cursor = self.cnx.cursor()
        if(tableName=="User"):
            insertionData = ("INSERT INTO " + tableName +
                   "(username, name, family, password , account)"
                   "VALUES (%s, %s, %s, %s ,%s)")
        elif(tableName=="Product"):
            insertionData = ("INSERT INTO " + tableName +
                   "(productCode, productType, price, stock)"
                   "VALUES (%s, %s, %s, %s)")
        elif(tableName=="GasSensor"):
            insertionData = ("INSERT INTO " + tableName +
                   "(username , productCode , time , CO2 , CO , CH4)"
                   "VALUES ( %s, %s, %s , %s , %s , %s)")
        elif(tableName=="TempSensor"):
            insertionData = ("INSERT INTO " + tableName +
                   " ( username , productCode , time , temperature)"
                   "VALUES (%s , %s , %s , %s)")
        elif(tableName=="HumiditySensor"):
            insertionData = ("INSERT INTO " + tableName +
                   "(username , productCode , time , airHumidity , soilHumidity)"
                   "VALUES (%s, %s, %s , %s , %s)")
        elif(tableName=="LightSensor"):
            insertionData = ("INSERT INTO " + tableName +
                   "(username , productCode , time , lightIntensity , bLightIntensity)"
                   "VALUES (%s, %s, %s , %s , %s)")
        else:
            print("TableName is unknown!")
        self.cursor.execute(insertionData, tableData)
        self.cnx.commit()


        self.cursor.close()
        self.cnx.close()




    def updateSensor(self, tableName , productID , data1 , data2 , data3 ):
        self.cnx = mysql.connector.connect(user=self.username , password=self.password , host=self.host , database=self.DB_NAME , port=self.PORT  )
        self.cursor = self.cnx.cursor()
        if(tableName=="GasSensor"):
            self.cursor.execute("""UPDATE GasSensor SET CO2 = %s , CO = %s , CH4 = %s WHERE productID= %s""" , (data1 , data2 , data3 , productID) )
        elif(tableName=="TempSensor"):
            self.cursor.execute("""UPDATE TempSensor SET temperature = %s WHERE productID= %s""" , (data1 , productID) )

        elif(tableName=="HumiditySensor"):
            self.cursor.execute("""UPDATE HumiditySensor SET (airHumidity , soilHumidity) = (%s , %s) WHERE productID= %s""" , (data1 , data2 , productID) )

        elif(tableName=="LightSensor"):
            self.cursor.execute("""UPDATE LightSensor SET (lightIntensity , bLightIntensity) = (%s , %s) WHERE productID= %s""" , (data1 , data2 ,  productID) )

        else:
            print("TableName is unknown!")
        self.cnx.commit()
        self.cursor.close()
        self.cnx.close()




    def insertRaw(self, username , product):
        insertionData = ("INSERT INTO " + product +
                   "(username , productCode , time)"
                   "VALUES (%s ,%s ,%s)")
        tableData = (username,self.getProductCode(product),Utilities.getFormattedDate())
        self.cnx = mysql.connector.connect(user=self.username , password=self.password , host=self.host , database=self.DB_NAME , port=self.PORT  )
        self.cursor = self.cnx.cursor()
        self.cursor.execute(insertionData, tableData)
        self.cnx.commit()
        self.cursor.close()
        self.cnx.close()



    def checkExistance(self,username):
        self.cnx = mysql.connector.connect(user=self.username , password=self.password , host=self.host , database=self.DB_NAME , port=self.PORT  )
        self.cursor = self.cnx.cursor()
        self.cursor.execute("""SELECT username FROM User WHERE username= %s""" , (username,))
        userTuple = (self.cursor.fetchall())
        self.cursor.close()
        self.cnx.close()
        if(userTuple):
            if userTuple[0][0] == username :
                return (1)
            else :
                return(0)
        else :
            return(0)





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


    def getGasSensors(self,username):
        self.cnx = mysql.connector.connect(user=self.username , password=self.password , host=self.host , database=self.DB_NAME , port=self.PORT  )
        self.cursor = self.cnx.cursor()
        self.cursor.execute("""SELECT * FROM GasSensor WHERE username=%s and CO2 is not null and CO is not null and CH4 is not null""" ,(username,))
        gasSensors = (self.cursor.fetchall())
        self.cursor.close()
        self.cnx.close()
        return (gasSensors)
    def getTempSensors(self,username):
        self.cnx = mysql.connector.connect(user=self.username , password=self.password , host=self.host , database=self.DB_NAME , port=self.PORT  )
        self.cursor = self.cnx.cursor()
        self.cursor.execute("""SELECT * FROM TempSensor WHERE username=%s and temperature is not null""" ,(username,))
        tempSensors = (self.cursor.fetchall())
        self.cursor.close()
        self.cnx.close()
        return (tempSensors)
    def getHumiditySensors(self,username):
        self.cnx = mysql.connector.connect(user=self.username , password=self.password , host=self.host , database=self.DB_NAME , port=self.PORT  )
        self.cursor = self.cnx.cursor()
        self.cursor.execute("""SELECT * FROM HumiditySensor WHERE username=%s and airHumidity is not null and soilHumidity is not null""" ,(username,))
        humiditySensors = (self.cursor.fetchall())
        self.cursor.close()
        self.cnx.close()
        return (humiditySensors)
    def getLightSensors(self,username):
        self.cnx = mysql.connector.connect(user=self.username , password=self.password , host=self.host , database=self.DB_NAME , port=self.PORT  )
        self.cursor = self.cnx.cursor()
        self.cursor.execute("""SELECT * FROM LightSensor WHERE username=%s and lightIntensity is not null and bLightIntensity is not null""" ,(username,))
        lightSensors = (self.cursor.fetchall())
        self.cursor.close()
        self.cnx.close()
        return (lightSensors)


    def getAllGasSensors(self):
        self.cnx = mysql.connector.connect(user=self.username , password=self.password , host=self.host , database=self.DB_NAME , port=self.PORT  )
        self.cursor = self.cnx.cursor()
        self.cursor.execute("""SELECT * FROM GasSensor""")
        gasSensors = (self.cursor.fetchall())
        self.cursor.close()
        self.cnx.close()
        return (gasSensors)
    def getAllTempSensors(self):
        self.cnx = mysql.connector.connect(user=self.username , password=self.password , host=self.host , database=self.DB_NAME , port=self.PORT  )
        self.cursor = self.cnx.cursor()
        self.cursor.execute("""SELECT * FROM TempSensor""")
        tempSensors = (self.cursor.fetchall())
        self.cursor.close()
        self.cnx.close()
        return (tempSensors)
    def getAllHumiditySensors(self):
        self.cnx = mysql.connector.connect(user=self.username , password=self.password , host=self.host , database=self.DB_NAME , port=self.PORT  )
        self.cursor = self.cnx.cursor()
        self.cursor.execute("""SELECT * FROM HumiditySensor""")
        humiditySensors = (self.cursor.fetchall())
        self.cursor.close()
        self.cnx.close()
        return (humiditySensors)
    def getAllLightSensors(self):
        self.cnx = mysql.connector.connect(user=self.username , password=self.password , host=self.host , database=self.DB_NAME , port=self.PORT  )
        self.cursor = self.cnx.cursor()
        self.cursor.execute("""SELECT * FROM LightSensor""")
        lightSensors = (self.cursor.fetchall())
        self.cursor.close()
        self.cnx.close()
        return (lightSensors)




    def sellDevices(self,username,product):
        if (self.getStock(product)):
            self.decStock(product)
            self.updateAccount(username,self.getPrice(product))
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



    def getPrice(self,product):
        self.cnx = mysql.connector.connect(user=self.username , password=self.password , host=self.host , database=self.DB_NAME , port=self.PORT  )
        self.cursor = self.cnx.cursor()
        self.cursor.execute("""SELECT price FROM Product WHERE productType= %s""" , (product,))
        priceTuple = (self.cursor.fetchall()[0])
        self.cursor.close()
        self.cnx.close()
        return (priceTuple[0])


    def updateAccount(self,username,amount):
        change = int(self.getAccount(username)) + amount
        self.cnx = mysql.connector.connect(user=self.username , password=self.password , host=self.host , database=self.DB_NAME , port=self.PORT  )
        self.cursor = self.cnx.cursor()
        self.cursor.execute("""UPDATE User SET account=%s WHERE username= %s""" , (change , username))
        self.cnx.commit()
        self.cursor.close()
        self.cnx.close()

    def getAccount(self,username):
        self.cnx = mysql.connector.connect(user=self.username , password=self.password , host=self.host , database=self.DB_NAME , port=self.PORT  )
        self.cursor = self.cnx.cursor()
        self.cursor.execute("""SELECT account FROM User WHERE username= %s""" , (username,))
        accountTuple = (self.cursor.fetchall()[0])
        self.cursor.close()
        self.cnx.close()
        return (accountTuple[0])



    def setPrice(self,product,amount):
        self.cnx = mysql.connector.connect(user=self.username , password=self.password , host=self.host , database=self.DB_NAME , port=self.PORT  )
        self.cursor = self.cnx.cursor()
        self.cursor.execute("""UPDATE Product SET price = %s WHERE productType= %s""" , (amount,product))
        self.cnx.commit()
        self.cursor.close()
        self.cnx.close()


    def checkUsername(self,username,password):
        self.cnx = mysql.connector.connect(user=self.username , password=self.password , host=self.host , database=self.DB_NAME , port=self.PORT  )
        self.cursor = self.cnx.cursor()
        self.cursor.execute("""SELECT password FROM User WHERE username= %s""" , (username,))
        accountTuple = (self.cursor.fetchall()[0])
        self.cursor.close()
        self.cnx.close()
        if password == accountTuple[0]:
            return (1)
        else:
            return (0)


    def checkOwnership(self,product , productID , username):
        self.cnx = mysql.connector.connect(user=self.username , password=self.password , host=self.host , database=self.DB_NAME , port=self.PORT  )
        self.cursor = self.cnx.cursor()
        self.cursor.execute("""SELECT username FROM %s WHERE productID= %s""" , (product,productID))
        userTuple = (self.cursor.fetchall())
        self.cursor.close()
        self.cnx.close()
        if(userTuple):
            if(username in userTuple):
                return (1)
            else:
                return (0)
        else:
            return (0)


    def getByQuery(self , text):
        self.cnx = mysql.connector.connect(user=self.username , password=self.password , host=self.host , database=self.DB_NAME , port=self.PORT  )
        self.cursor = self.cnx.cursor()
        self.cursor.execute(text)

        if("select" in text):
            resultTuple = (self.cursor.fetchall())
            self.cursor.close()
            self.cnx.close()
            return (True, resultTuple)
        else:
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return (False, ("insertion successful"))

