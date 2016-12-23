import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication , QLabel
import MainUpdator
from Utilities import getInformation as info



u = MainUpdator.Updator()
class Example(QMainWindow):



    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        label1 = QLabel(self)
        label1.setText(("Gas Sensors : %s" % (u.getStock("GasSensor"),)))
        label1.move(60,20)
        label1.setFixedWidth(200)
        label2 = QLabel(self)
        label2.setText(("Temperature Sensors : %s" % (u.getStock("TempSensor"),)))
        label2.move(60,40)
        label2.setFixedWidth(200)
        label3 = QLabel(self)
        label3.setText(("Humidity Sensors : %s" % (u.getStock("HumiditySensor"),)))
        label3.move(60,60)
        label3.setFixedWidth(200)
        label4 = QLabel(self)
        label4.setText(("Light Sensors : %s" %  (u.getStock("LightSensor"),)))
        label4.move(60,80)
        label4.setFixedWidth(200)

        add1 = QPushButton("+", self)
        add1.move(10, 25)
        add1.setAccessibleName("GasSensor")
        dec1 = QPushButton("-", self)
        dec1.move(30, 25)
        dec1.setAccessibleName("GasSensor")
        add1.setFixedSize(15,15)
        dec1.setFixedSize(15,15)
        add2 = QPushButton("+", self)
        add2.move(10, 45)
        add2.setAccessibleName("TempSensor")
        dec2 = QPushButton("-", self)
        dec2.move(30, 45)
        dec2.setAccessibleName("TempSensor")
        add2.setFixedSize(15,15)
        dec2.setFixedSize(15,15)
        add3 = QPushButton("+", self)
        add3.move(10, 65)
        add3.setAccessibleName("HumiditySensor")
        dec3 = QPushButton("-", self)
        dec3.move(30, 65)
        dec3.setAccessibleName("HumiditySensor")
        add3.setFixedSize(15,15)
        dec3.setFixedSize(15,15)
        add4 = QPushButton("+", self)
        add4.move(10, 85)
        add4.setAccessibleName("LightSensor")
        dec4 = QPushButton("-", self)
        dec4.move(30, 85)
        dec4.setAccessibleName("LightSensor")
        add4.setFixedSize(15,15)
        dec4.setFixedSize(15,15)

        add1.clicked.connect(self.buttonClicked)
        dec1.clicked.connect(self.buttonClicked)
        add2.clicked.connect(self.buttonClicked)
        dec2.clicked.connect(self.buttonClicked)
        add3.clicked.connect(self.buttonClicked)
        dec3.clicked.connect(self.buttonClicked)
        add4.clicked.connect(self.buttonClicked)
        dec4.clicked.connect(self.buttonClicked)




        self.statusBar()
        self.setFixedSize(600,600)
        self.setWindowTitle('IOT Shop')
        self.show()


    def buttonClicked(self):
        sender = self.sender()
        if(sender.text()=="+"):
           u.incStock(sender.accessibleName())
        elif(sender.text()=="-"):
           u.decStock(sender.accessibleName())
        self.updateGUI(sender)


    def updateGUI(self,sender):
         self.close()
         self.initUI()







def window():
    QApplication.processEvents()
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())










