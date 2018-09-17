# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Cliente/Vista/ClientMainView.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
import sys
import os
import socket
import time
import random
from PyQt5 import QtCore, QtGui, QtWidgets

sys.path.insert(1, os.path.join(sys.path[0], '../..'))
from Cliente.Vista.ClientMainViewController import ClientMainViewController
from shared.Connection import Connection

class Ui_ClientMainWindow(object):

    def __init__(self):
        self.controller = ClientMainViewController(self)
        self.randPort = random.randint(5001,5999)

    def setupUi(self, ClientMainWindow):
        ClientMainWindow.setObjectName("ClientMainWindow")
        ClientMainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(ClientMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.brokerIpLabel = QtWidgets.QLabel(self.centralwidget)
        self.brokerIpLabel.setGeometry(QtCore.QRect(30, 20, 59, 16))
        self.brokerIpLabel.setObjectName("brokerIpLabel")
        self.brokerIpLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.brokerIpLineEdit.setGeometry(QtCore.QRect(100, 20, 291, 21))
        self.brokerIpLineEdit.setObjectName("brokerIpLineEdit")
        self.brokerPortLabel = QtWidgets.QLabel(self.centralwidget)
        self.brokerPortLabel.setGeometry(QtCore.QRect(410, 20, 81, 16))
        self.brokerPortLabel.setObjectName("brokerPortLabel")
        self.brokerPortSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.brokerPortSpinBox.setGeometry(QtCore.QRect(490, 20, 301, 22))
        self.brokerPortSpinBox.setMaximum(99999)
        self.brokerPortSpinBox.setObjectName("brokerPortSpinBox")
        self.nameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nameLineEdit.setGeometry(QtCore.QRect(100, 60, 291, 21))
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setGeometry(QtCore.QRect(30, 60, 59, 16))
        self.nameLabel.setObjectName("nameLabel")
        self.residenceLabel = QtWidgets.QLabel(self.centralwidget)
        self.residenceLabel.setGeometry(QtCore.QRect(410, 60, 71, 16))
        self.residenceLabel.setObjectName("residenceLabel")
        self.residenceLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.residenceLineEdit.setGeometry(QtCore.QRect(490, 60, 291, 21))
        self.residenceLineEdit.setObjectName("residenceLineEdit")
        self.myIpLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.myIpLineEdit.setGeometry(QtCore.QRect(100, 100, 291, 21))
        self.myIpLineEdit.setText(socket.gethostbyname(socket.gethostname()))
        self.myIpLineEdit.setObjectName("myIpLineEdit")
        self.myIpLabel = QtWidgets.QLabel(self.centralwidget)
        self.myIpLabel.setGeometry(QtCore.QRect(30, 100, 59, 16))
        self.myIpLabel.setObjectName("myIpLabel")
        self.myPortLabel = QtWidgets.QLabel(self.centralwidget)
        self.myPortLabel.setGeometry(QtCore.QRect(410, 100, 71, 16))
        self.myPortLabel.setObjectName("myPortLabel")
        self.myPortSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.myPortSpinBox.setGeometry(QtCore.QRect(490, 100, 301, 22))
        self.myPortSpinBox.setMaximum(99999)
        self.myPortSpinBox.setObjectName("myPortSpinBox")
        self.myPortSpinBox.setValue(self.randPort)
        self.familyCompLabel = QtWidgets.QLabel(self.centralwidget)
        self.familyCompLabel.setGeometry(QtCore.QRect(30, 130, 291, 16))
        self.familyCompLabel.setObjectName("familyCompLabel")
        self.familyCompLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.familyCompLineEdit.setGeometry(QtCore.QRect(320, 130, 461, 21))
        self.familyCompLineEdit.setText("")
        self.familyCompLineEdit.setObjectName("familyCompLineEdit")
        self.inundacionesCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.inundacionesCheckBox.setGeometry(QtCore.QRect(190, 170, 101, 20))
        self.inundacionesCheckBox.setObjectName("inundacionesCheckBox")
        self.categoryLabel = QtWidgets.QLabel(self.centralwidget)
        self.categoryLabel.setGeometry(QtCore.QRect(130, 170, 59, 16))
        self.categoryLabel.setObjectName("categoryLabel")
        self.vendabalesCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.vendabalesCheckBox.setGeometry(QtCore.QRect(310, 170, 101, 20))
        self.vendabalesCheckBox.setObjectName("vendabalesCheckBox")
        self.incendiosCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.incendiosCheckBox.setGeometry(QtCore.QRect(430, 170, 101, 20))
        self.incendiosCheckBox.setObjectName("incendiosCheckBox")
        self.derrumbesCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.derrumbesCheckBox.setGeometry(QtCore.QRect(550, 170, 101, 20))
        self.derrumbesCheckBox.setObjectName("derrumbesCheckBox")
        self.subscribePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.subscribePushButton.setGeometry(QtCore.QRect(130, 200, 511, 32))
        self.subscribePushButton.setObjectName("subscribePushButton")
        self.newsFeedTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.newsFeedTextEdit.setGeometry(QtCore.QRect(10, 260, 781, 271))
        self.newsFeedTextEdit.setObjectName("newsFeedTextEdit")
        self.newsLabel = QtWidgets.QLabel(self.centralwidget)
        self.newsLabel.setGeometry(QtCore.QRect(10, 240, 71, 16))
        self.newsLabel.setObjectName("newsLabel")
        ClientMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ClientMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        ClientMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ClientMainWindow)
        self.statusbar.setObjectName("statusbar")
        ClientMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ClientMainWindow)
        QtCore.QMetaObject.connectSlotsByName(ClientMainWindow)

        # Connect buttons
        self.makeButtonsConnections()

        # Initialize Thread
        self.getNewsThread = GetNewsThread(self.randPort)
        self.getNewsThread.start()
        self.getNewsThread.signal.connect(self.appendMessage)



    def appendMessage(self, newMessage):
        print(newMessage)
        self.newsFeedTextEdit.append(str(newMessage))


    def retranslateUi(self, ClientMainWindow):
        _translate = QtCore.QCoreApplication.translate
        ClientMainWindow.setWindowTitle(_translate("ClientMainWindow", "MainWindow"))
        self.brokerIpLabel.setText(_translate("ClientMainWindow", "Borker IP:"))
        self.brokerPortLabel.setText(_translate("ClientMainWindow", "Borker Port:"))
        self.nameLabel.setText(_translate("ClientMainWindow", "Nombre:"))
        self.residenceLabel.setText(_translate("ClientMainWindow", "Residencia:"))
        self.myIpLabel.setText(_translate("ClientMainWindow", "Mi IP:"))
        self.myPortLabel.setText(_translate("ClientMainWindow", "Mi Puerto:"))
        self.familyCompLabel.setText(_translate("ClientMainWindow", "Composición Familiar (Separado Por Comas \',\'):"))
        self.inundacionesCheckBox.setText(_translate("ClientMainWindow", "Inundaciones"))
        self.categoryLabel.setText(_translate("ClientMainWindow", "Temas:"))
        self.vendabalesCheckBox.setText(_translate("ClientMainWindow", "Vendabales"))
        self.incendiosCheckBox.setText(_translate("ClientMainWindow", "Incendios"))
        self.derrumbesCheckBox.setText(_translate("ClientMainWindow", "Derrumbes"))
        self.subscribePushButton.setText(_translate("ClientMainWindow", "Subscribe"))
        self.newsLabel.setText(_translate("ClientMainWindow", "Noticias"))

    def getBrokerData(self):
        broker_data = {
            'ip_broker': self.brokerIpLineEdit.text(),
            'port_broker': int(self.brokerPortSpinBox.value())
        }
        return  broker_data

    def getUserData(self):
        composicion_familiar = self.familyCompLineEdit.text().split(',')
        temas = [self.inundacionesCheckBox.isChecked(),
                 self.vendabalesCheckBox.isChecked(),
                 self.incendiosCheckBox.isChecked(),
                 self.derrumbesCheckBox.isChecked()]
        user_data = {
            'nombre': self.nameLineEdit.text(),
            'residencia': self.residenceLineEdit.text(),
            'ip': self.myIpLineEdit.text(),
            'puerto': int(self.myPortSpinBox.value()),
            'comp_familiar': composicion_familiar,
            'temas': temas
        }
        return  user_data

    def makeButtonsConnections(self):
        self.subscribePushButton.clicked.connect(self.controller.subscribePushButtonHandler)

class GetNewsThread(QtCore.QThread):
    signal = QtCore.pyqtSignal('PyQt_PyObject')
    def __init__(self, listening_port, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.conn = Connection('127.0.0.1', listening_port)
        self.BUFFER = 1024
    def run(self):
        i = 0
        while True:
            #msg = self.conn.listen(self.BUFFER)
            self.signal.emit(i)
            i+=1
            time.sleep(5)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ClientMainWindow = QtWidgets.QMainWindow()
    ui = Ui_ClientMainWindow()
    ui.setupUi(ClientMainWindow)
    ClientMainWindow.show()
    sys.exit(app.exec_())

