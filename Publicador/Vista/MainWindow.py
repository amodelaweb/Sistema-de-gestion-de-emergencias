# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Publicador/Vista/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets

sys.path.insert(1, os.path.join(sys.path[0], '../..'))
from Publicador.Vista.MainWindowController import MainWindowController

class Ui_MainWindow(object):

    def __init__(self):
        self.controller = MainWindowController(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(676, 516)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.brokerIpLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.brokerIpLineEdit.setGeometry(QtCore.QRect(80, 20, 141, 21))
        self.brokerIpLineEdit.setClearButtonEnabled(False)
        self.brokerIpLineEdit.setObjectName("brokerIpLineEdit")
        self.connectPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectPushButton.setGeometry(QtCore.QRect(13, 50, 651, 32))
        self.connectPushButton.setObjectName("connectPushButton")
        self.prokerIpLabel = QtWidgets.QLabel(self.centralwidget)
        self.prokerIpLabel.setGeometry(QtCore.QRect(10, 20, 59, 16))
        self.prokerIpLabel.setObjectName("prokerIpLabel")
        self.portLabel = QtWidgets.QLabel(self.centralwidget)
        self.portLabel.setGeometry(QtCore.QRect(230, 20, 59, 16))
        self.portLabel.setObjectName("portLabel")
        self.prokerPortLineEdit = QtWidgets.QSpinBox(self.centralwidget)
        self.prokerPortLineEdit.setGeometry(QtCore.QRect(280, 20, 101, 21))
        self.prokerPortLineEdit.setObjectName("prokerPortLineEdit")
        self.prokerPortLineEdit.setMaximum(9999)
        self.sourceNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.sourceNameLabel.setGeometry(QtCore.QRect(400, 20, 101, 16))
        self.sourceNameLabel.setObjectName("sourceNameLabel")
        self.sourceNameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.sourceNameLineEdit.setGeometry(QtCore.QRect(510, 20, 141, 21))
        self.sourceNameLineEdit.setObjectName("sourceNameLineEdit")
        self.stateLabel = QtWidgets.QLabel(self.centralwidget)
        self.stateLabel.setGeometry(QtCore.QRect(20, 80, 631, 16))
        self.stateLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.stateLabel.setObjectName("stateLabel")
        self.bodyTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.bodyTextEdit.setGeometry(QtCore.QRect(10, 120, 651, 231))
        self.bodyTextEdit.setDocumentTitle("")
        self.bodyTextEdit.setObjectName("bodyTextEdit")
        self.bodyLabel = QtWidgets.QLabel(self.centralwidget)
        self.bodyLabel.setGeometry(QtCore.QRect(10, 100, 59, 16))
        self.bodyLabel.setObjectName("bodyLabel")
        self.authorLabel = QtWidgets.QLabel(self.centralwidget)
        self.authorLabel.setGeometry(QtCore.QRect(10, 360, 59, 16))
        self.authorLabel.setObjectName("authorLabel")
        self.authorLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.authorLineEdit.setGeometry(QtCore.QRect(60, 360, 601, 21))
        self.authorLineEdit.setObjectName("authorLineEdit")
        self.inundacionesCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.inundacionesCheckBox.setGeometry(QtCore.QRect(70, 410, 101, 20))
        self.inundacionesCheckBox.setObjectName("inundacionesCheckBox")
        self.categoryLabel = QtWidgets.QLabel(self.centralwidget)
        self.categoryLabel.setGeometry(QtCore.QRect(10, 410, 59, 16))
        self.categoryLabel.setObjectName("categoryLabel")
        self.vendabalesCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.vendabalesCheckBox.setGeometry(QtCore.QRect(190, 410, 101, 20))
        self.vendabalesCheckBox.setObjectName("vendabalesCheckBox")
        self.incendiosCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.incendiosCheckBox.setGeometry(QtCore.QRect(310, 410, 101, 20))
        self.incendiosCheckBox.setObjectName("incendiosCheckBox")
        self.derrumbesCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.derrumbesCheckBox.setGeometry(QtCore.QRect(430, 410, 101, 20))
        self.derrumbesCheckBox.setObjectName("derrumbesCheckBox")
        self.sendPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendPushButton.setGeometry(QtCore.QRect(10, 430, 651, 32))
        self.sendPushButton.setObjectName("sendPushButton")
        self.loadJsonPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadJsonPushButton.setGeometry(QtCore.QRect(540, 400, 114, 32))
        self.loadJsonPushButton.setObjectName("loadJsonPushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 676, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Add methods to buttons
        self.makeButtonsConnections()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.connectPushButton.setText(_translate("MainWindow", "Conectar"))
        self.prokerIpLabel.setText(_translate("MainWindow", "Broker IP:"))
        self.portLabel.setText(_translate("MainWindow", "Puerto:"))
        self.sourceNameLabel.setText(_translate("MainWindow", "Nombre Fuente"))
        self.stateLabel.setText(_translate("MainWindow", "Sin Conectar..."))
        self.bodyLabel.setText(_translate("MainWindow", "Noticia:"))
        self.authorLabel.setText(_translate("MainWindow", "Autor:"))
        self.inundacionesCheckBox.setText(_translate("MainWindow", "Inundaciones"))
        self.categoryLabel.setText(_translate("MainWindow", "Temas:"))
        self.vendabalesCheckBox.setText(_translate("MainWindow", "Vendabales"))
        self.incendiosCheckBox.setText(_translate("MainWindow", "Incendios"))
        self.derrumbesCheckBox.setText(_translate("MainWindow", "Derrumbes"))
        self.loadJsonPushButton.setText(_translate("MainWindow", "Cargar JSON"))
        self.sendPushButton.setText(_translate("MainWindow", "¡Enviar!"))

    def getBrokerData(self):
        broker_data = {
            'ip_broker': self.brokerIpLineEdit.text(),
            'port_broker': int(self.prokerPortLineEdit.value()),
            'nombre': self.sourceNameLineEdit.text()
        }
        return  broker_data

    def getNewsData(self):
        temas = [self.inundacionesCheckBox.isChecked(), self.vendabalesCheckBox.isChecked(),self.incendiosCheckBox.isChecked(), self.derrumbesCheckBox.isChecked()]
        news_data = {
            'body': self.bodyTextEdit.toPlainText(),
            'author': self.authorLineEdit.text(),
            'temas': temas
        }
        return  news_data

    def getFilePath(self):
        window = QtWidgets.QWidget()
        window.setGeometry(10, 10, 640, 480)
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(window, "QFileDialog.getOpenFileName()", "", "All Files (*);;JSON Files (*.json)",options=options)
        if fileName:
            return fileName
        window.show()


    def makeButtonsConnections(self):
        self.connectPushButton.clicked.connect(self.controller.connectPushButtonHandler)
        self.sendPushButton.clicked.connect(self.controller.sendPushButtonHandler)
        self.loadJsonPushButton.clicked.connect(self.controller.loadJsonPushButtonHandler)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

