import mysql.connector
import MainUpdator
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
        "  `time` date,"
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
        "  `time` date,"
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
        "  `time` date,"
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
