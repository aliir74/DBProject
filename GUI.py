import sys
import time
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication , QLabel , QWidget
import MainUpdator
from Utilities import getInformation as info





u = MainUpdator.Updator()




app = QApplication(sys.argv)
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

def buttonClicked():
   if(window.sender().text()=="+"):
      u.incStock(window.sender().accessibleName())
   elif(window.sender().text()=="-"):
      u.decStock(window.sender().accessibleName())
   updateGUI()

add1.clicked.connect(buttonClicked)
dec1.clicked.connect(buttonClicked)
add2.clicked.connect(buttonClicked)
dec2.clicked.connect(buttonClicked)
add3.clicked.connect(buttonClicked)
dec3.clicked.connect(buttonClicked)
add4.clicked.connect(buttonClicked)
dec4.clicked.connect(buttonClicked)




def updateGUI():
   label1.setText(("Gas Sensors : %s" % (u.getStock("GasSensor"),)))
   label2.setText(("Temperature Sensors : %s" % (u.getStock("TempSensor"),)))
   label3.setText(("Humidity Sensors : %s" % (u.getStock("HumiditySensor"),)))
   label4.setText(("Light Sensors : %s" %  (u.getStock("LightSensor"),)))





window.show()

sys.exit(app.exec())


























