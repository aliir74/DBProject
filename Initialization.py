import mysql.connector
import MainUpdator
import Utilities
from mysql.connector import errorcode

user = 'testuser'
password = 'test123test!'

def create(DB_NAME , PORT) :

    cnx = mysql.connector.connect(user=user , password=password , host='localhost' , port=PORT)
    cursor = cnx.cursor()




    def create_database(cursor):
        try:
            cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)

    try:
        cnx.database = DB_NAME
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor)
            cnx.database = DB_NAME
        else:
            print(err)
            exit(1)





    TABLES = {}
    TABLES[0] = (
        "CREATE TABLE `User` ("
        "  `username` varchar(20) ,"
        "  `name` varchar(20),"
        "  `family` varchar(20),"
        "  `password` varchar(20),"
        "  `account` int(20),"
        "  PRIMARY KEY (`username`)"
        ") ENGINE=InnoDB")

    TABLES[1] = (
        "CREATE TABLE `Product` ("
        "  `productCode` int(10),"
        "  `productType` varchar(40),"
        "  `price` int(10),"
        "  `stock` int(10),"
        "  PRIMARY KEY (`productCode`)"
        ") ENGINE=InnoDB")

    TABLES[2] = (
        "CREATE TABLE `TempSensor` ("
        "  `productID` int(10) AUTO_INCREMENT,"
        "  `username` varchar(20),"
        "  `productCode` int(10),"
        "  `time` timestamp ,"
        "  `temperature` int(10),"
        "  PRIMARY KEY (`productID`), "
        "  FOREIGN KEY (`username`)"
        "  REFERENCES `User` (`username`),"
        "  FOREIGN KEY (`productCode`)"
        "  REFERENCES `Product` (`productCode`)"
        ") ENGINE=InnoDB")

    TABLES[3] = (
        "CREATE TABLE `LightSensor` ("
        "  `productID` int(10) AUTO_INCREMENT ,"
        "  `username` varchar(20),"
        "  `productCode` int(10),"
        "  `time` timestamp,"
        "  `lightIntensity` int(10),"
        "  `bLightIntensity` int(10),"
        "  PRIMARY KEY (`productID`), "
        "  FOREIGN KEY (`username`)"
        "  REFERENCES `User` (`username`),"
        "  FOREIGN KEY (`productCode`)"
        "  REFERENCES `Product` (`productCode`)"
        ") ENGINE=InnoDB")

    TABLES[4] = (
        "  CREATE TABLE `HumiditySensor` ("
        "  `productID` int(10) AUTO_INCREMENT ,"
        "  `username` varchar(20),"
        "  `productCode` int(10),"
        "  `time` timestamp,"
        "  `airHumidity` int(10),"
        "  `soilHumidity` int(10),"
        "  PRIMARY KEY (`productID`), "
        "  FOREIGN KEY (`username`)"
        "  REFERENCES `User` (`username`),"
        "  FOREIGN KEY (`productCode`)"
        "  REFERENCES `Product` (`productCode`)"
        ") ENGINE=InnoDB")

    TABLES[5] = (
        "  CREATE TABLE `GasSensor` ("
        "  `productID` int(10) AUTO_INCREMENT ,"
        "  `username` varchar(20)  ,"
        "  `productCode` int(10),"
        "  `time` timestamp,"
        "  `CO2` int(10),"
        "  `CO` int(10),"
        "  `CH4` int(10),"
        "  PRIMARY KEY (`productID`), "
        "  FOREIGN KEY (`username`)"
        "  REFERENCES `User` (`username`),"
        "  FOREIGN KEY (`productCode`)"
        "  REFERENCES `Product` (`productCode`)"
        ") ENGINE=InnoDB")



    for i, ddl in TABLES.items():
        try:
            print("Creating table {}: ".format(i))
            cursor.execute(ddl)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

    cursor.close()
    cnx.close()


    u = MainUpdator.Updator(user,password,'localhost',DB_NAME,PORT)
    u.insert("Product" , ("0" , "Actuator" , "2500" , "0"))
    u.insert("Product" , ("1" , "GasSensor" , "1500" , "0"))
    u.insert("Product" , ("2" , "TempSensor" , "1000" , "0"))
    u.insert("Product" , ("3" , "HumiditySensor" , "1000" , "0"))
    u.insert("Product" , ("4" , "LightSensor" , "500" , "0"))

    u.insert("User" , ("mxii1994" , "Mehdi" , "Safaee" , "mono1728" , "0"))
    u.insert("User" , ("ali94" , "Ali" , "Irani" , "ali0241" , "0"))
    u.insert("User" , ("HN93" , "Hossein" , "Nazari" , "hn93" , "0"))
    u.insert("User" , ("MRTZSLAV1993" , "MohammadReza" , "Mortezavi" , "mrtzslav1993" , "0"))
    u.insert("User" , ("Marya94" , "Maryam" , "Farahani" , "m1994" , "0"))

    u.setStock("GasSensor" , "20")
    u.setStock("TempSensor" , "20")
    u.setStock("HumiditySensor" , "20")
    u.setStock("LightSensor" , "20")

    u.insert("GasSensor" , ("MRTZSLAV1993" , "1" , Utilities.getFormattedDate() , "20" , "20" , "20"))
    u.insert("GasSensor" , ("MRTZSLAV1993" , "1" , Utilities.getFormattedDate() , "25" , "25" , "25"))
    u.insert("TempSensor" , ("mxii1994" , "2" , Utilities.getFormattedDate() , "30"))
    u.insert("HumiditySensor" , ("mxii1994" , "3" , Utilities.getFormattedDate() , "60" , "60"))
    u.insert("LightSensor" , ("mxii1994" , "4" , Utilities.getFormattedDate() , "5" , "5"))
    u.insert("LightSensor" , ("mxii1994" , "4" , Utilities.getFormattedDate() , "10" , "10"))

    u.sellDevices("mxii1994" , "TempSensor")
    u.sellDevices("mxii1994" , "TempSensor")
    u.sellDevices("mxii1994" , "TempSensor")
    u.sellDevices("mxii1994" , "LightSensor")
    u.sellDevices("Marya94" , "LightSensor")
    u.sellDevices("Marya94" , "LightSensor")
    u.sellDevices("MRTZSLAV1993" , "GasSensor")
    u.sellDevices("MRTZSLAV1993" , "GasSensor")