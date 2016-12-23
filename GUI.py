import sys
import time
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication , QLabel , QWidget , QInputDialog , QMessageBox , QLineEdit
import MainUpdator
from Utilities import getInformation as info





u = MainUpdator.Updator()




app = QApplication(sys.argv)
window = QMainWindow()
window.setFixedSize(350,180)
window.setWindowTitle('IOT Shop')

label1 = QLabel(window)
label1.setText(("Gas Sensors : %s" % (u.getStock("GasSensor"),)))
label1.move(60,10)
label1.setFixedWidth(200)
label2 = QLabel(window)
label2.setText(("Temperature Sensors : %s" % (u.getStock("TempSensor"),)))
label2.move(60,30)
label2.setFixedWidth(200)
label3 = QLabel(window)
label3.setText(("Humidity Sensors : %s" % (u.getStock("HumiditySensor"),)))
label3.move(60,50)
label3.setFixedWidth(200)
label4 = QLabel(window)
label4.setText(("Light Sensors : %s" %  (u.getStock("LightSensor"),)))
label4.move(60,70)
label4.setFixedWidth(200)

add1 = QPushButton("+", window)
add1.move(20, 18)
add1.setAccessibleName("GasSensor")
dec1 = QPushButton("-", window)
dec1.move(35, 18)
dec1.setAccessibleName("GasSensor")
add1.setFixedSize(15,15)
dec1.setFixedSize(15,15)
add2 = QPushButton("+", window)
add2.move(20, 38)
add2.setAccessibleName("TempSensor")
dec2 = QPushButton("-", window)
dec2.move(35, 38)
dec2.setAccessibleName("TempSensor")
add2.setFixedSize(15,15)
dec2.setFixedSize(15,15)
add3 = QPushButton("+", window)
add3.move(20, 58)
add3.setAccessibleName("HumiditySensor")
dec3 = QPushButton("-", window)
dec3.move(35, 58)
dec3.setAccessibleName("HumiditySensor")
add3.setFixedSize(15,15)
dec3.setFixedSize(15,15)
add4 = QPushButton("+", window)
add4.move(20, 78)
add4.setAccessibleName("LightSensor")
dec4 = QPushButton("-", window)
dec4.move(35, 78)
dec4.setAccessibleName("LightSensor")
add4.setFixedSize(15,15)
dec4.setFixedSize(15,15)



set1 = QPushButton("Set", window)
set1.move(270, 15)
set1.setAccessibleName("GasSensor")
set1.setFixedSize(30,20)
set2 = QPushButton("Set", window)
set2.move(270, 35)
set2.setAccessibleName("TempSensor")
set2.setFixedSize(30,20)
set3 = QPushButton("Set", window)
set3.move(270, 55)
set3.setAccessibleName("HumiditySensor")
set3.setFixedSize(30,20)
set4 = QPushButton("Set", window)
set4.move(270, 75)
set4.setAccessibleName("LightSensor")
set4.setFixedSize(30,20)


sell1 = QPushButton("Sell", window)
sell1.move(300, 15)
sell1.setAccessibleName("GasSensor")
sell1.setFixedSize(30,20)
sell2 = QPushButton("Sell", window)
sell2.move(300, 35)
sell2.setAccessibleName("TempSensor")
sell2.setFixedSize(30,20)
sell3 = QPushButton("Sell", window)
sell3.move(300, 55)
sell3.setAccessibleName("HumiditySensor")
sell3.setFixedSize(30,20)
sell4 = QPushButton("Sell", window)
sell4.move(300, 75)
sell4.setAccessibleName("LightSensor")
sell4.setFixedSize(30,20)




opt1 = QPushButton("Get User Account", window)
opt1.move(5, 100)
opt1.setAccessibleName("opt1")
opt1.setFixedSize(175,45)
opt2 = QPushButton("Register New User", window)
opt2.move(170, 100)
opt2.setAccessibleName("opt2")
opt2.setFixedSize(175,45)
opt3 = QPushButton("Sensors by Type", window)
opt3.move(5, 135)
opt3.setAccessibleName("opt3")
opt3.setFixedSize(175,45)
opt4 = QPushButton("Sensors by Username", window)
opt4.move(170, 135)
opt4.setAccessibleName("opt4")
opt4.setFixedSize(175,45)






























def buttonClicked1():
   if(window.sender().text()=="+"):
      u.incStock(window.sender().accessibleName())
   elif(window.sender().text()=="-"):
      u.decStock(window.sender().accessibleName())
   updateGUI()



add1.clicked.connect(buttonClicked1)
dec1.clicked.connect(buttonClicked1)
add2.clicked.connect(buttonClicked1)
dec2.clicked.connect(buttonClicked1)
add3.clicked.connect(buttonClicked1)
dec3.clicked.connect(buttonClicked1)
add4.clicked.connect(buttonClicked1)
dec4.clicked.connect(buttonClicked1)




def buttonClicked2():
   text = getText("Selling ..." , "Enter Customers Username")
   if(u.checkExistance(text)):
      u.sellDevices(text,window.sender().accessibleName())
   updateGUI()



sell1.clicked.connect(buttonClicked2)
sell2.clicked.connect(buttonClicked2)
sell3.clicked.connect(buttonClicked2)
sell4.clicked.connect(buttonClicked2)




def buttonClicked3():
   text = getText("set Stock ..." , "Enter Stock Value")
   try:
      val = int(text)
      if((text) and (int(text) > 0)):
         u.setStock(window.sender().accessibleName(),int(text))
   except ValueError:
      print("That's not an int!")
   updateGUI()



set1.clicked.connect(buttonClicked3)
set2.clicked.connect(buttonClicked3)
set3.clicked.connect(buttonClicked3)
set4.clicked.connect(buttonClicked3)





def optClicked1():
   text = getText("Get User Info ..." , "Enter Customers Username")
   if(u.checkExistance(text)):
      message(text + " totaly paid : " + str(u.getAccount(text)))
   else:
      message("user doesnt exist")
   updateGUI()



def optClicked2():
   text = getText("Register New Users ..." , "Enter Registration Username")
   if(u.checkExistance(text)):
      message("user already exists")
   else:
      getUserData = GetUserData
      getUserData.showPanel(getUserData)
   updateGUI()



def optClicked3():
   text = getText("Get Sensors by Type ..." , "Enter Sensor Type")
   if(u.checkExistance(text)):
      u.sellDevices(text,window.sender().accessibleName())
   updateGUI()



def optClicked4():
   text = getText("Get Sensors by Username ..." , "Enter Username")
   if(u.checkExistance(text)):
      print("opt4")
   else:
      message("username doesnt exist")
   updateGUI()






opt1.clicked.connect(optClicked1)
opt2.clicked.connect(optClicked2)
opt3.clicked.connect(optClicked3)
opt4.clicked.connect(optClicked4)


























def updateGUI():
   label1.setText(("Gas Sensors : %s" % (u.getStock("GasSensor"),)))
   label2.setText(("Temperature Sensors : %s" % (u.getStock("TempSensor"),)))
   label3.setText(("Humidity Sensors : %s" % (u.getStock("HumiditySensor"),)))
   label4.setText(("Light Sensors : %s" %  (u.getStock("LightSensor"),)))






def getText(headerBar , textBar):
   text, ok = QInputDialog.getText(window, headerBar, textBar)

   if ok:
      return text



def message(text):
   msg = QMessageBox(window)
   msg.setText(text)
   msg.setWindowTitle("something went wrong")
   msg.show()








class GetUserData():

   data = ""
   panel = QWidget()
   panel.setWindowTitle("Registration")
   panel.setFixedSize(250,250)
   label1 = QLabel(panel)
   label2 = QLabel(panel)
   label3 = QLabel(panel)
   label4 = QLabel(panel)
   label1.setText("username")
   label1.move(20,25)
   label2.setText("Name")
   label2.move(20,75)
   label3.setText("Family")
   label3.move(20,125)
   label4.setText("Password")
   label4.move(20,175)

   textField1 = QLineEdit(panel)
   textField2 = QLineEdit(panel)
   textField3 = QLineEdit(panel)
   textField4 = QLineEdit(panel)

   textField1.move(100 , 25)
   textField2.move(100 , 75)
   textField3.move(100 , 125)
   textField4.move(100 , 175)


   button1 = QPushButton("OK" , panel)
   button1.move(60,210)
   button1.setFixedSize(50 , 20)
   button2 = QPushButton("Cancel" , panel)
   button2.move(140,210)
   button2.setFixedSize(50 , 20)


   def option1(self):
      GetUserData.panel.hide()
      u.insert("User" , (GetUserData.textField1.text() , GetUserData.textField2.text() , GetUserData.textField3.text() , GetUserData.textField4.text() , "0"))


   def option2(self):
      GetUserData.panel.hide()
      print(GetUserData.data)

   button1.clicked.connect( option1 )
   button2.clicked.connect( option2 )






   def showPanel(self):
      self.panel.show()

   def getUserName(self):
        return 1
























window.show()

sys.exit(app.exec())


























