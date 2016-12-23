import sys
import time
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication , QLabel , QWidget , QInputDialog
import MainUpdator
from Utilities import getInformation as info





u = MainUpdator.Updator()




app = QApplication(sys.argv)
getInput = QInputDialog
window = QMainWindow()
window.setFixedSize(600,600)
window.setWindowTitle('IOT Shop')

label1 = QLabel(window)
label1.setText(("Gas Sensors : %s" % (u.getStock("GasSensor"),)))
label1.move(60,20)
label1.setFixedWidth(200)
label2 = QLabel(window)
label2.setText(("Temperature Sensors : %s" % (u.getStock("TempSensor"),)))
label2.move(60,40)
label2.setFixedWidth(200)
label3 = QLabel(window)
label3.setText(("Humidity Sensors : %s" % (u.getStock("HumiditySensor"),)))
label3.move(60,60)
label3.setFixedWidth(200)
label4 = QLabel(window)
label4.setText(("Light Sensors : %s" %  (u.getStock("LightSensor"),)))
label4.move(60,80)
label4.setFixedWidth(200)

add1 = QPushButton("+", window)
add1.move(10, 25)
add1.setAccessibleName("GasSensor")
dec1 = QPushButton("-", window)
dec1.move(30, 25)
dec1.setAccessibleName("GasSensor")
add1.setFixedSize(15,15)
dec1.setFixedSize(15,15)
add2 = QPushButton("+", window)
add2.move(10, 45)
add2.setAccessibleName("TempSensor")
dec2 = QPushButton("-", window)
dec2.move(30, 45)
dec2.setAccessibleName("TempSensor")
add2.setFixedSize(15,15)
dec2.setFixedSize(15,15)
add3 = QPushButton("+", window)
add3.move(10, 65)
add3.setAccessibleName("HumiditySensor")
dec3 = QPushButton("-", window)
dec3.move(30, 65)
dec3.setAccessibleName("HumiditySensor")
add3.setFixedSize(15,15)
dec3.setFixedSize(15,15)
add4 = QPushButton("+", window)
add4.move(10, 85)
add4.setAccessibleName("LightSensor")
dec4 = QPushButton("-", window)
dec4.move(30, 85)
dec4.setAccessibleName("LightSensor")
add4.setFixedSize(15,15)
dec4.setFixedSize(15,15)



set1 = QPushButton("Set", window)
set1.move(250, 25)
set1.setAccessibleName("GasSensor")
set1.setFixedSize(30,20)
set2 = QPushButton("Set", window)
set2.move(250, 45)
set2.setAccessibleName("TempSensor")
set2.setFixedSize(30,20)
set3 = QPushButton("Set", window)
set3.move(250, 65)
set3.setAccessibleName("HumiditySensor")
set3.setFixedSize(30,20)
set4 = QPushButton("Set", window)
set4.move(250, 85)
set4.setAccessibleName("LightSensor")
set4.setFixedSize(30,20)


sell1 = QPushButton("Sell", window)
sell1.move(300, 25)
sell1.setAccessibleName("GasSensor")
sell1.setFixedSize(30,20)
sell2 = QPushButton("Sell", window)
sell2.move(300, 45)
sell2.setAccessibleName("TempSensor")
sell2.setFixedSize(30,20)
sell3 = QPushButton("Sell", window)
sell3.move(300, 65)
sell3.setAccessibleName("HumiditySensor")
sell3.setFixedSize(30,20)
sell4 = QPushButton("Sell", window)
sell4.move(300, 85)
sell4.setAccessibleName("LightSensor")
sell4.setFixedSize(30,20)




































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
   print(int(text))
   if((text) and int(text)>0):
      u.setStock(window.sender().accessibleName(),int(text))
   updateGUI()



set1.clicked.connect(buttonClicked3)
set2.clicked.connect(buttonClicked3)
set3.clicked.connect(buttonClicked3)
set4.clicked.connect(buttonClicked3)






def updateGUI():
   label1.setText(("Gas Sensors : %s" % (u.getStock("GasSensor"),)))
   label2.setText(("Temperature Sensors : %s" % (u.getStock("TempSensor"),)))
   label3.setText(("Humidity Sensors : %s" % (u.getStock("HumiditySensor"),)))
   label4.setText(("Light Sensors : %s" %  (u.getStock("LightSensor"),)))






def getText(headerBar , textBar):
   text, ok = QInputDialog.getText(window, headerBar, textBar)

   if ok:
      print(text)
      return text











window.show()

sys.exit(app.exec())


























