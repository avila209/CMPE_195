# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyQT5_GUI_480P.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import obd

#Made connection a global variable to be able to pass to shut-down function for closing
connection = None

#00:1D:A5:03:E8:51

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-image: url(:/newPrefix/Background_480p.png)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MPHLabel = QtWidgets.QLabel(self.centralwidget)
        self.MPHLabel.setGeometry(QtCore.QRect(354, 165, 90, 64))
        font = QtGui.QFont()
        font.setFamily("SteelfishRg-Regular")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.MPHLabel.setFont(font)
        self.MPHLabel.setStyleSheet("QLabel{\n"
"    background:  rgba( 255, 255, 255, 0% );\n"
"    color: rgb(255,255,255);\n"
"}")
        self.MPHLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.MPHLabel.setObjectName("MPHLabel")
        self.RPMLabel = QtWidgets.QLabel(self.centralwidget)
        self.RPMLabel.setGeometry(QtCore.QRect(354, 264, 86, 56))
        font = QtGui.QFont()
        font.setFamily("SteelfishRg-Regular")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(50)
        self.RPMLabel.setFont(font)
        self.RPMLabel.setStyleSheet("QLabel{\n"
"    background:  rgba( 255, 255, 255, 0% );\n"
"    color: rgb(255,255,255);\n"
"}")
        self.RPMLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.RPMLabel.setObjectName("RPMLabel")
        self.Gas_1 = QtWidgets.QFrame(self.centralwidget)
        self.Gas_1.setGeometry(QtCore.QRect(141, 321, 74, 3))
        self.Gas_1.setLineWidth(3)
        self.Gas_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.Gas_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Gas_1.setObjectName("Gas_1")
        self.Gas_2 = QtWidgets.QFrame(self.centralwidget)
        self.Gas_2.setGeometry(QtCore.QRect(135, 306, 74, 3))
        self.Gas_2.setLineWidth(3)
        self.Gas_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.Gas_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Gas_2.setObjectName("Gas_2")
        self.Gas_3 = QtWidgets.QFrame(self.centralwidget)
        self.Gas_3.setGeometry(QtCore.QRect(126, 291, 74, 3))
        self.Gas_3.setLineWidth(3)
        self.Gas_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.Gas_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Gas_3.setObjectName("Gas_3")
        self.Gas_4 = QtWidgets.QFrame(self.centralwidget)
        self.Gas_4.setGeometry(QtCore.QRect(120, 276, 74, 3))
        self.Gas_4.setLineWidth(3)
        self.Gas_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.Gas_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Gas_4.setObjectName("Gas_4")
        self.Gas_5 = QtWidgets.QFrame(self.centralwidget)
        self.Gas_5.setGeometry(QtCore.QRect(111, 261, 74, 3))
        self.Gas_5.setLineWidth(3)
        self.Gas_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.Gas_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Gas_5.setObjectName("Gas_5")
        self.Gas_6 = QtWidgets.QFrame(self.centralwidget)
        self.Gas_6.setGeometry(QtCore.QRect(105, 246, 74, 3))
        self.Gas_6.setLineWidth(3)
        self.Gas_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.Gas_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Gas_6.setObjectName("Gas_6")
        self.Gas_7 = QtWidgets.QFrame(self.centralwidget)
        self.Gas_7.setGeometry(QtCore.QRect(99, 234, 74, 3))
        self.Gas_7.setLineWidth(3)
        self.Gas_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.Gas_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Gas_7.setObjectName("Gas_7")
        self.Temp_3 = QtWidgets.QFrame(self.centralwidget)
        self.Temp_3.setGeometry(QtCore.QRect(597, 294, 74, 3))
        self.Temp_3.setLineWidth(3)
        self.Temp_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.Temp_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Temp_3.setObjectName("Temp_3")
        self.Temp_5 = QtWidgets.QFrame(self.centralwidget)
        self.Temp_5.setGeometry(QtCore.QRect(609, 264, 74, 3))
        self.Temp_5.setLineWidth(3)
        self.Temp_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.Temp_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Temp_5.setObjectName("Temp_5")
        self.Temp_6 = QtWidgets.QFrame(self.centralwidget)
        self.Temp_6.setGeometry(QtCore.QRect(618, 249, 74, 3))
        self.Temp_6.setLineWidth(3)
        self.Temp_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.Temp_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Temp_6.setObjectName("Temp_6")
        self.Temp_2 = QtWidgets.QFrame(self.centralwidget)
        self.Temp_2.setGeometry(QtCore.QRect(588, 306, 74, 3))
        self.Temp_2.setLineWidth(3)
        self.Temp_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.Temp_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Temp_2.setObjectName("Temp_2")
        self.Temp_7 = QtWidgets.QFrame(self.centralwidget)
        self.Temp_7.setGeometry(QtCore.QRect(624, 234, 74, 3))
        self.Temp_7.setLineWidth(3)
        self.Temp_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.Temp_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Temp_7.setObjectName("Temp_7")
        self.Temp_4 = QtWidgets.QFrame(self.centralwidget)
        self.Temp_4.setGeometry(QtCore.QRect(603, 279, 74, 3))
        self.Temp_4.setLineWidth(3)
        self.Temp_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.Temp_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Temp_4.setObjectName("Temp_4")
        self.Temp_1 = QtWidgets.QFrame(self.centralwidget)
        self.Temp_1.setGeometry(QtCore.QRect(582, 321, 74, 3))
        self.Temp_1.setLineWidth(3)
        self.Temp_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.Temp_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Temp_1.setObjectName("Temp_1")
        self.BSS_Right = QtWidgets.QLabel(self.centralwidget)
        self.BSS_Right.setGeometry(QtCore.QRect(624, 100, 100, 100))
        self.BSS_Right.setText("")
        self.BSS_Right.setPixmap(QtGui.QPixmap(":/newPrefix/blindspot copy.png"))
        self.BSS_Right.setScaledContents(True)
        self.BSS_Right.setObjectName("BSS_Right")
        self.BSS_Left = QtWidgets.QLabel(self.centralwidget)
        self.BSS_Left.setGeometry(QtCore.QRect(72, 100, 100, 100))
        self.BSS_Left.setText("")
        self.BSS_Left.setPixmap(QtGui.QPixmap(":/newPrefix/blindspot_2.png"))
        self.BSS_Left.setScaledContents(True)
        self.BSS_Left.setObjectName("BSS_Left")
        self.BSS_Right_On = QtWidgets.QLabel(self.centralwidget)
        self.BSS_Right_On.setGeometry(QtCore.QRect(624, 100, 100, 100))
        self.BSS_Right_On.setText("")
        self.BSS_Right_On.setPixmap(QtGui.QPixmap(":/newPrefix/blindspot_yellow_right.png"))
        self.BSS_Right_On.setScaledContents(True)
        self.BSS_Right_On.setObjectName("BSS_Right_On")
        self.BSS_Left_On = QtWidgets.QLabel(self.centralwidget)
        self.BSS_Left_On.setGeometry(QtCore.QRect(72, 100, 100, 100))
        self.BSS_Left_On.setText("")
        self.BSS_Left_On.setPixmap(QtGui.QPixmap(":/newPrefix/blindspot_yellow_left.png"))
        self.BSS_Left_On.setScaledContents(True)
        self.BSS_Left_On.setObjectName("BSS_Left_On")
        self.MPH_0 = QtWidgets.QLabel(self.centralwidget)
        self.MPH_0.setGeometry(QtCore.QRect(330, 350, 13, 13))
        self.MPH_0.setText("")
        self.MPH_0.setPixmap(QtGui.QPixmap(":/newPrefix/Speedo indicator.png"))
        self.MPH_0.setScaledContents(True)
        self.MPH_0.setObjectName("MPH_0")
        self.MPH_1 = QtWidgets.QLabel(self.centralwidget)
        self.MPH_1.setGeometry(QtCore.QRect(288, 321, 13, 13))
        self.MPH_1.setText("")
        self.MPH_1.setPixmap(QtGui.QPixmap(":/newPrefix/Speedo indicator.png"))
        self.MPH_1.setScaledContents(True)
        self.MPH_1.setObjectName("MPH_1")
        self.MPH_2 = QtWidgets.QLabel(self.centralwidget)
        self.MPH_2.setGeometry(QtCore.QRect(264, 285, 13, 13))
        self.MPH_2.setText("")
        self.MPH_2.setPixmap(QtGui.QPixmap(":/newPrefix/Speedo indicator.png"))
        self.MPH_2.setScaledContents(True)
        self.MPH_2.setObjectName("MPH_2")
        self.MPH_3 = QtWidgets.QLabel(self.centralwidget)
        self.MPH_3.setGeometry(QtCore.QRect(250, 240, 13, 13))
        self.MPH_3.setText("")
        self.MPH_3.setPixmap(QtGui.QPixmap(":/newPrefix/Speedo indicator.png"))
        self.MPH_3.setScaledContents(True)
        self.MPH_3.setObjectName("MPH_3")
        self.MPH_4 = QtWidgets.QLabel(self.centralwidget)
        self.MPH_4.setGeometry(QtCore.QRect(252, 192, 13, 13))
        self.MPH_4.setText("")
        self.MPH_4.setPixmap(QtGui.QPixmap(":/newPrefix/Speedo indicator.png"))
        self.MPH_4.setScaledContents(True)
        self.MPH_4.setObjectName("MPH_4")
        self.MPH_5 = QtWidgets.QLabel(self.centralwidget)
        self.MPH_5.setGeometry(QtCore.QRect(276, 144, 13, 13))
        self.MPH_5.setText("")
        self.MPH_5.setPixmap(QtGui.QPixmap(":/newPrefix/Speedo indicator.png"))
        self.MPH_5.setScaledContents(True)
        self.MPH_5.setObjectName("MPH_5")
        self.MPH_6 = QtWidgets.QLabel(self.centralwidget)
        self.MPH_6.setGeometry(QtCore.QRect(306, 108, 13, 13))
        self.MPH_6.setText("")
        self.MPH_6.setPixmap(QtGui.QPixmap(":/newPrefix/Speedo indicator.png"))
        self.MPH_6.setScaledContents(True)
        self.MPH_6.setObjectName("MPH_6")
        self.MPH_7 = QtWidgets.QLabel(self.centralwidget)
        self.MPH_7.setGeometry(QtCore.QRect(345, 84, 13, 13))
        self.MPH_7.setText("")
        self.MPH_7.setPixmap(QtGui.QPixmap(":/newPrefix/Speedo indicator.png"))
        self.MPH_7.setScaledContents(True)
        self.MPH_7.setObjectName("MPH_7")
        self.MPH_8 = QtWidgets.QLabel(self.centralwidget)
        self.MPH_8.setGeometry(QtCore.QRect(393, 75, 13, 13))
        self.MPH_8.setText("")
        self.MPH_8.setPixmap(QtGui.QPixmap(":/newPrefix/Speedo indicator.png"))
        self.MPH_8.setScaledContents(True)
        self.MPH_8.setObjectName("MPH_8")
        self.MPH_9 = QtWidgets.QLabel(self.centralwidget)
        self.MPH_9.setGeometry(QtCore.QRect(441, 87, 13, 13))
        self.MPH_9.setText("")
        self.MPH_9.setPixmap(QtGui.QPixmap(":/newPrefix/Speedo indicator.png"))
        self.MPH_9.setScaledContents(True)
        self.MPH_9.setObjectName("MPH_9")
        self.MPH_10 = QtWidgets.QLabel(self.centralwidget)
        self.MPH_10.setGeometry(QtCore.QRect(483, 108, 13, 13))
        self.MPH_10.setText("")
        self.MPH_10.setPixmap(QtGui.QPixmap(":/newPrefix/Speedo indicator.png"))
        self.MPH_10.setScaledContents(True)
        self.MPH_10.setObjectName("MPH_10")
        self.MPH_11 = QtWidgets.QLabel(self.centralwidget)
        self.MPH_11.setGeometry(QtCore.QRect(516, 144, 13, 13))
        self.MPH_11.setText("")
        self.MPH_11.setPixmap(QtGui.QPixmap(":/newPrefix/Speedo indicator.png"))
        self.MPH_11.setScaledContents(True)
        self.MPH_11.setObjectName("MPH_11")
        self.MPH_12 = QtWidgets.QLabel(self.centralwidget)
        self.MPH_12.setGeometry(QtCore.QRect(534, 189, 13, 13))
        self.MPH_12.setText("")
        self.MPH_12.setPixmap(QtGui.QPixmap(":/newPrefix/Speedo indicator.png"))
        self.MPH_12.setScaledContents(True)
        self.MPH_12.setObjectName("MPH_12")
        self.MPH_13 = QtWidgets.QLabel(self.centralwidget)
        self.MPH_13.setGeometry(QtCore.QRect(537, 237, 13, 13))
        self.MPH_13.setText("")
        self.MPH_13.setPixmap(QtGui.QPixmap(":/newPrefix/Speedo indicator.png"))
        self.MPH_13.setScaledContents(True)
        self.MPH_13.setObjectName("MPH_13")
        self.MPH_14 = QtWidgets.QLabel(self.centralwidget)
        self.MPH_14.setGeometry(QtCore.QRect(522, 285, 13, 13))
        self.MPH_14.setText("")
        self.MPH_14.setPixmap(QtGui.QPixmap(":/newPrefix/Speedo indicator.png"))
        self.MPH_14.setScaledContents(True)
        self.MPH_14.setObjectName("MPH_14")
        self.MPH_15 = QtWidgets.QLabel(self.centralwidget)
        self.MPH_15.setGeometry(QtCore.QRect(495, 321, 13, 13))
        self.MPH_15.setText("")
        self.MPH_15.setPixmap(QtGui.QPixmap(":/newPrefix/Speedo indicator.png"))
        self.MPH_15.setScaledContents(True)
        self.MPH_15.setObjectName("MPH_15")
        self.MPH_16 = QtWidgets.QLabel(self.centralwidget)
        self.MPH_16.setGeometry(QtCore.QRect(456, 351, 13, 13))
        self.MPH_16.setText("")
        self.MPH_16.setPixmap(QtGui.QPixmap(":/newPrefix/Speedo indicator.png"))
        self.MPH_16.setScaledContents(True)
        self.MPH_16.setObjectName("MPH_16")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(696, 438, 93, 28))
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton.setStyleSheet("background: rgb(104, 104, 104)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Shut Down")
        self.retranslateUi(MainWindow)

        self.pushButton.clicked.connect(self.closeIt)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.MPHLabel.setText(_translate("MainWindow", "120"))
        self.RPMLabel.setText(_translate("MainWindow", "7600"))

    def closeIt(self):
        message = QMessageBox()
        message.setWindowTitle("Powering Off")
        message.setText("Safetly shutting down the OS")
        message.setIcon(QMessageBox.Information)
        
        x = message.exec_()

        connection.stop()
        connection.close()
        #os.system("sudo shutdown -h now") #Instant
        #os.system("sudo shutdown") #Safe
        self.close()


        
import xz_4
import time
import sys, os


speed = None
rpm = None
temp = None
fuel = None


def get_speed(s):
    if not s.is_null():
        global speed
        speed = int(s.value.magnitude * .621)
        print("MPH = ", speed)

def get_rpm(r):
    if not r.is_null():
        global rpm
        rpm = int(r.value.magnitude)
        print("RPM = ", rpm)

def get_temp(t):
    if not t.is_null():
        global temp
        temp = int(t.value.magnitude)
        print("Temp = ", temp)

def get_fuel(f):
    if not f.is_null():
        global fuel
        fuel = int(f.value.magnitude)
        print("Fuel = ", fuel)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show() #For laptop testing
    #MainWindow.showFullScreen() #Full screen for RPI 7inch display

    ''' Testing values '''
    ui.Gas_1.hide()
    ui.Gas_2.hide()
    ui.Gas_3.hide()
    ui.Gas_4.hide()
    ui.Gas_5.hide()
    ui.Gas_6.hide()
    ui.Gas_7.hide()

    ui.Temp_1.hide()
    ui.Temp_2.hide()
    ui.Temp_3.hide()
    ui.Temp_4.hide()
    ui.Temp_5.hide()
    ui.Temp_6.hide()
    ui.Temp_7.hide()

    ui.BSS_Left_On.hide()
    ui.BSS_Right_On.hide()

    ui.MPH_0.hide()
    ui.MPH_1.hide()
    ui.MPH_2.hide()
    ui.MPH_3.hide()
    ui.MPH_4.hide()
    ui.MPH_5.hide()
    ui.MPH_6.hide()
    ui.MPH_7.hide()
    ui.MPH_8.hide()
    ui.MPH_9.hide()
    ui.MPH_10.hide()
    ui.MPH_11.hide()
    ui.MPH_12.hide()
    ui.MPH_13.hide()
    ui.MPH_14.hide()
    ui.MPH_15.hide()
    ui.MPH_16.hide()

    #Setup Window Message
    setup = QMessageBox()
    setup.setWindowTitle("Setup")
    setup.setText("Please connect the OBD Scanner and turn on the vehicle. \nClick OK to continue.")
    setup.setIcon(QMessageBox.Information)
    x = setup.exec_()
    
    #Insert bluetooth commands here .... using os.system("") or subprocess

    #Using subprocess: subprocess.check_output(['ls', '-l'])
    '''import subprocess
    cmd = ['/run/myscript', '--arg', 'value']
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    for line in p.stdout:
        print line
    p.wait()
    print p.returncod
    '''
    #subprocess.call(["command1", "arg1", "arg2"])

    #After bluetooth and rfcomm commands: Setup OBD Connection
    connection = obd.Async(fast=False)

    ''' USED FOR TESTING/DEMONSTRATION OF THE UI -- EXPO
    rpm = 0
    for i in range(181):
        sleep(0.05)
        rpm = i * 50
        ui.MPHLabel.setText(str(i))
        ui.RPMLabel.setText(str(rpm))
        app.processEvents()

        if(i > 0):
            ui.MPH_0.show()
        if(i > 10):
            ui.MPH_1.show()
        if(i > 20):
            ui.Gas_1.show()
            ui.Temp_1.show()
            ui.MPH_2.show()
        if(i > 30):
            ui.MPH_3.show()
        if(i > 40):
            ui.Gas_2.show()
            ui.Temp_2.show()
            ui.MPH_4.show()
        if(i > 50):
            ui.MPH_5.show()
        if(i > 60):
            ui.Gas_3.show()
            ui.Temp_3.show()
            ui.MPH_6.show()
        if(i > 70):
            ui.MPH_7.show()
        if(i > 80):
            ui.Gas_4.show()
            ui.Temp_4.show()

            ui.BSS_Left_On.show()
            ui.BSS_Right_On.show()

            ui.MPH_8.show()
        if(i > 90):
            ui.MPH_9.show()
        if(i > 100):
            ui.Gas_5.show()
            ui.Temp_5.show()

            ui.BSS_Left_On.hide()
            ui.BSS_Right_On.hide()

            ui.MPH_10.show()
        if(i > 110):
            ui.MPH_11.show()
        if(i > 120):
            ui.Gas_6.show()
            ui.Temp_6.show()
            ui.MPH_12.show()
        if(i > 130):
            ui.MPH_13.show()
        if(i > 140):
            ui.Gas_7.show()
            ui.Temp_7.show()
            ui.MPH_14.show()
        if(i > 150):
            ui.MPH_15.show()
        if(i > 160):
            ui.MPH_16.show()
    '''

    connection.watch(obd.commands.SPEED, callback=get_speed)
    connection.watch(obd.commands.RPM, callback=get_rpm)
    connection.watch(obd.commands.COOLANT_TEMP, callback=get_temp)
    connection.watch(obd.commands.FUEL_LEVEL, callback=get_fuel)

    connection.start()
    
    running = True
    while running:
        time.sleep(.5)
        if(speed != None):
            ui.MPHLabel.setText(str(speed))
            if(speed >= 0 and speed < 10):
                ui.MPH_0.show()
                ui.MPH_1.hide()
                ui.MPH_2.hide()
                ui.MPH_3.hide()
                ui.MPH_4.hide()
                ui.MPH_5.hide()
                ui.MPH_6.hide()
                ui.MPH_7.hide()
                ui.MPH_8.hide()
                ui.MPH_9.hide()
                ui.MPH_10.hide()
                ui.MPH_11.hide()
                ui.MPH_12.hide()
                ui.MPH_13.hide()
                ui.MPH_14.hide()
                ui.MPH_15.hide()
                ui.MPH_16.hide()
            if(speed >= 10 and speed < 20):
                ui.MPH_0.show()
                ui.MPH_1.show()
                ui.MPH_2.hide()
                ui.MPH_3.hide()
                ui.MPH_4.hide()
                ui.MPH_5.hide()
                ui.MPH_6.hide()
                ui.MPH_7.hide()
                ui.MPH_8.hide()
                ui.MPH_9.hide()
                ui.MPH_10.hide()
                ui.MPH_11.hide()
                ui.MPH_12.hide()
                ui.MPH_13.hide()
                ui.MPH_14.hide()
                ui.MPH_15.hide()
                ui.MPH_16.hide()
            if(speed >= 20 and speed < 30):
                ui.MPH_0.show()
                ui.MPH_1.show()
                ui.MPH_2.show()
                ui.MPH_3.hide()
                ui.MPH_4.hide()
                ui.MPH_5.hide()
                ui.MPH_6.hide()
                ui.MPH_7.hide()
                ui.MPH_8.hide()
                ui.MPH_9.hide()
                ui.MPH_10.hide()
                ui.MPH_11.hide()
                ui.MPH_12.hide()
                ui.MPH_13.hide()
                ui.MPH_14.hide()
                ui.MPH_15.hide()
                ui.MPH_16.hide()
            if(speed >= 30 and speed < 40):
                ui.MPH_0.show()
                ui.MPH_1.show()
                ui.MPH_2.show()
                ui.MPH_3.show()
                ui.MPH_4.hide()
                ui.MPH_5.hide()
                ui.MPH_6.hide()
                ui.MPH_7.hide()
                ui.MPH_8.hide()
                ui.MPH_9.hide()
                ui.MPH_10.hide()
                ui.MPH_11.hide()
                ui.MPH_12.hide()
                ui.MPH_13.hide()
                ui.MPH_14.hide()
                ui.MPH_15.hide()
                ui.MPH_16.hide()
            if(speed >= 40 and speed < 50):
                ui.MPH_0.show()
                ui.MPH_1.show()
                ui.MPH_2.show()
                ui.MPH_3.show()
                ui.MPH_4.show()
                ui.MPH_5.hide()
                ui.MPH_6.hide()
                ui.MPH_7.hide()
                ui.MPH_8.hide()
                ui.MPH_9.hide()
                ui.MPH_10.hide()
                ui.MPH_11.hide()
                ui.MPH_12.hide()
                ui.MPH_13.hide()
                ui.MPH_14.hide()
                ui.MPH_15.hide()
                ui.MPH_16.hide()
            if(speed >= 50 and speed < 60):
                ui.MPH_0.show()
                ui.MPH_1.show()
                ui.MPH_2.show()
                ui.MPH_3.show()
                ui.MPH_4.show()
                ui.MPH_5.show()
                ui.MPH_6.hide()
                ui.MPH_7.hide()
                ui.MPH_8.hide()
                ui.MPH_9.hide()
                ui.MPH_10.hide()
                ui.MPH_11.hide()
                ui.MPH_12.hide()
                ui.MPH_13.hide()
                ui.MPH_14.hide()
                ui.MPH_15.hide()
                ui.MPH_16.hide()
            if(speed >= 60 and speed < 70):
                ui.MPH_0.show()
                ui.MPH_1.show()
                ui.MPH_2.show()
                ui.MPH_3.show()
                ui.MPH_4.show()
                ui.MPH_5.show()
                ui.MPH_6.show()
                ui.MPH_7.hide()
                ui.MPH_8.hide()
                ui.MPH_9.hide()
                ui.MPH_10.hide()
                ui.MPH_11.hide()
                ui.MPH_12.hide()
                ui.MPH_13.hide()
                ui.MPH_14.hide()
                ui.MPH_15.hide()
                ui.MPH_16.hide()
            if(speed >= 70 and speed < 80):
                ui.MPH_0.show()
                ui.MPH_1.show()
                ui.MPH_2.show()
                ui.MPH_3.show()
                ui.MPH_4.show()
                ui.MPH_5.show()
                ui.MPH_6.show()
                ui.MPH_7.show()
                ui.MPH_8.hide()
                ui.MPH_9.hide()
                ui.MPH_10.hide()
                ui.MPH_11.hide()
                ui.MPH_12.hide()
                ui.MPH_13.hide()
                ui.MPH_14.hide()
                ui.MPH_15.hide()
                ui.MPH_16.hide()
            if(speed >= 80 and speed < 90):
                ui.MPH_0.show()
                ui.MPH_1.show()
                ui.MPH_2.show()
                ui.MPH_3.show()
                ui.MPH_4.show()
                ui.MPH_5.show()
                ui.MPH_6.show()
                ui.MPH_7.show()
                ui.MPH_8.show()
                ui.MPH_9.hide()
                ui.MPH_10.hide()
                ui.MPH_11.hide()
                ui.MPH_12.hide()
                ui.MPH_13.hide()
                ui.MPH_14.hide()
                ui.MPH_15.hide()
                ui.MPH_16.hide()
            if(speed >= 90 and speed < 100):
                ui.MPH_0.show()
                ui.MPH_1.show()
                ui.MPH_2.show()
                ui.MPH_3.show()
                ui.MPH_4.show()
                ui.MPH_5.show()
                ui.MPH_6.show()
                ui.MPH_7.show()
                ui.MPH_8.show()
                ui.MPH_9.show()
                ui.MPH_10.hide()
                ui.MPH_11.hide()
                ui.MPH_12.hide()
                ui.MPH_13.hide()
                ui.MPH_14.hide()
                ui.MPH_15.hide()
                ui.MPH_16.hide()
            if(speed >= 100 and speed < 110):
                ui.MPH_0.show()
                ui.MPH_1.show()
                ui.MPH_2.show()
                ui.MPH_3.show()
                ui.MPH_4.show()
                ui.MPH_5.show()
                ui.MPH_6.show()
                ui.MPH_7.show()
                ui.MPH_8.show()
                ui.MPH_9.show()
                ui.MPH_10.show()
                ui.MPH_11.hide()
                ui.MPH_12.hide()
                ui.MPH_13.hide()
                ui.MPH_14.hide()
                ui.MPH_15.hide()
                ui.MPH_16.hide()
            if(speed >= 110 and speed < 120):
                ui.MPH_0.show()
                ui.MPH_1.show()
                ui.MPH_2.show()
                ui.MPH_3.show()
                ui.MPH_4.show()
                ui.MPH_5.show()
                ui.MPH_6.show()
                ui.MPH_7.show()
                ui.MPH_8.show()
                ui.MPH_9.show()
                ui.MPH_10.show()
                ui.MPH_11.show()
                ui.MPH_12.hide()
                ui.MPH_13.hide()
                ui.MPH_14.hide()
                ui.MPH_15.hide()
                ui.MPH_16.hide()
            if(speed >= 120 and speed < 130):
                ui.MPH_0.show()
                ui.MPH_1.show()
                ui.MPH_2.show()
                ui.MPH_3.show()
                ui.MPH_4.show()
                ui.MPH_5.show()
                ui.MPH_6.show()
                ui.MPH_7.show()
                ui.MPH_8.show()
                ui.MPH_9.show()
                ui.MPH_10.show()
                ui.MPH_11.show()
                ui.MPH_12.show()
                ui.MPH_13.hide()
                ui.MPH_14.hide()
                ui.MPH_15.hide()
                ui.MPH_16.hide()
            if(speed >= 130 and speed < 140):
                ui.MPH_0.show()
                ui.MPH_1.show()
                ui.MPH_2.show()
                ui.MPH_3.show()
                ui.MPH_4.show()
                ui.MPH_5.show()
                ui.MPH_6.show()
                ui.MPH_7.show()
                ui.MPH_8.show()
                ui.MPH_9.show()
                ui.MPH_10.show()
                ui.MPH_11.show()
                ui.MPH_12.show()
                ui.MPH_13.show()
                ui.MPH_14.hide()
                ui.MPH_15.hide()
                ui.MPH_16.hide()
            if(speed >= 140 and speed < 150):
                ui.MPH_0.show()
                ui.MPH_1.show()
                ui.MPH_2.show()
                ui.MPH_3.show()
                ui.MPH_4.show()
                ui.MPH_5.show()
                ui.MPH_6.show()
                ui.MPH_7.show()
                ui.MPH_8.show()
                ui.MPH_9.show()
                ui.MPH_10.show()
                ui.MPH_11.show()
                ui.MPH_12.show()
                ui.MPH_13.show()
                ui.MPH_14.show()
                ui.MPH_15.hide()
                ui.MPH_16.hide()
            if(speed >= 150 and speed < 160):
                ui.MPH_0.show()
                ui.MPH_1.show()
                ui.MPH_2.show()
                ui.MPH_3.show()
                ui.MPH_4.show()
                ui.MPH_5.show()
                ui.MPH_6.show()
                ui.MPH_7.show()
                ui.MPH_8.show()
                ui.MPH_9.show()
                ui.MPH_10.show()
                ui.MPH_11.show()
                ui.MPH_12.show()
                ui.MPH_13.show()
                ui.MPH_14.show()
                ui.MPH_15.show()
                ui.MPH_16.hide()
            if(speed >= 160):
                ui.MPH_0.show()
                ui.MPH_1.show()
                ui.MPH_2.show()
                ui.MPH_3.show()
                ui.MPH_4.show()
                ui.MPH_5.show()
                ui.MPH_6.show()
                ui.MPH_7.show()
                ui.MPH_8.show()
                ui.MPH_9.show()
                ui.MPH_10.show()
                ui.MPH_11.show()
                ui.MPH_12.show()
                ui.MPH_13.show()
                ui.MPH_14.show()
                ui.MPH_15.show()
                ui.MPH_16.show()
            
        if(rpm != None):
            ui.RPMLabel.setText(str(rpm))
        if(temp != None):
            if(temp < 60):
                ui.Temp_1.show()
                ui.Temp_2.hide()
                ui.Temp_3.hide()
                ui.Temp_4.hide()
                ui.Temp_5.hide()
                ui.Temp_6.hide()
                ui.Temp_7.hide()

            if(temp >= 60 and temp < 70):
                ui.Temp_1.show()
                ui.Temp_2.show()
                ui.Temp_3.show()
                ui.Temp_4.hide()
                ui.Temp_5.hide()
                ui.Temp_6.hide()
                ui.Temp_7.hide()

            if(temp >= 70 and temp < 80):
                ui.Temp_1.show()
                ui.Temp_2.show()
                ui.Temp_3.hide()
                ui.Temp_4.hide()
                ui.Temp_5.hide()
                ui.Temp_6.hide()
                ui.Temp_7.hide()
                
            if(temp >= 80 and temp < 90):
                ui.Temp_1.show()
                ui.Temp_2.show()
                ui.Temp_3.show()
                ui.Temp_4.show()
                ui.Temp_5.hide()
                ui.Temp_6.hide()
                ui.Temp_7.hide()

            if(temp >= 90 and temp < 100):
                ui.Temp_1.show()
                ui.Temp_2.show()
                ui.Temp_3.show()
                ui.Temp_4.show()
                ui.Temp_5.show()
                ui.Temp_6.hide()
                ui.Temp_7.hide()

            if(temp >= 100 and temp < 110):
                ui.Temp_1.show()
                ui.Temp_2.show()
                ui.Temp_3.show()
                ui.Temp_4.show()
                ui.Temp_5.show()
                ui.Temp_6.show()
                ui.Temp_7.hide()

            if(temp >= 110):
                ui.Temp_1.show()
                ui.Temp_2.show()
                ui.Temp_3.show()
                ui.Temp_4.show()
                ui.Temp_5.show()
                ui.Temp_6.show()
                ui.Temp_7.show()
                
        if(fuel != None):
            if(fuel < 14.25):
                ui.Gas_1.show()
                ui.Gas_2.hide()
                ui.Gas_3.hide()
                ui.Gas_4.hide()
                ui.Gas_5.hide()
                ui.Gas_6.hide()
                ui.Gas_7.hide()

            if(fuel >= 14.25 and fuel < 28.5):
                ui.Gas_1.show()
                ui.Gas_2.show()
                ui.Gas_3.hide()
                ui.Gas_4.hide()
                ui.Gas_5.hide()
                ui.Gas_6.hide()
                ui.Gas_7.hide()

            if(fuel >= 28.5 and fuel < 42.75):
                ui.Gas_1.show()
                ui.Gas_2.show()
                ui.Gas_3.show()
                ui.Gas_4.hide()
                ui.Gas_5.hide()
                ui.Gas_6.hide()
                ui.Gas_7.hide()
                
            if(fuel >= 42.75 and fuel < 57):
                ui.Gas_1.show()
                ui.Gas_2.show()
                ui.Gas_3.show()
                ui.Gas_4.show()
                ui.Gas_5.hide()
                ui.Gas_6.hide()
                ui.Gas_7.hide()

            if(fuel >= 57 and fuel < 71.25):
                ui.Gas_1.show()
                ui.Gas_2.show()
                ui.Gas_3.show()
                ui.Gas_4.show()
                ui.Gas_5.show()
                ui.Gas_6.hide()
                ui.Gas_7.hide()

            if(fuel >= 71.25 and fuel < 85.5):
                ui.Gas_1.show()
                ui.Gas_2.show()
                ui.Gas_3.show()
                ui.Gas_4.show()
                ui.Gas_5.show()
                ui.Gas_6.show()
                ui.Gas_7.hide()

            if(fuel >= 95):
                ui.Gas_1.show()
                ui.Gas_2.show()
                ui.Gas_3.show()
                ui.Gas_4.show()
                ui.Gas_5.show()
                ui.Gas_6.show()
                ui.Gas_7.show()
        
        
        app.processEvents()
    
            
    sys.exit(app.exec_())
