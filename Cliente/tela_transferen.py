# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_transferen(object):
    def setupUi(self, Tela_transferen):
        Tela_transferen.setObjectName("Tela_transferen")
        Tela_transferen.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(Tela_transferen)
        self.centralwidget.setObjectName("centralwidget")
        self.Valor = QtWidgets.QLabel(self.centralwidget)
        self.Valor.setGeometry(QtCore.QRect(160, 180, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Valor.setFont(font)
        self.Valor.setObjectName("Valor")
        self.Transfe = QtWidgets.QLabel(self.centralwidget)
        self.Transfe.setGeometry(QtCore.QRect(200, 70, 180, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Transfe.setFont(font)
        self.Transfe.setObjectName("Transfe")
        self.ButTrans = QtWidgets.QPushButton(self.centralwidget)
        self.ButTrans.setGeometry(QtCore.QRect(240, 270, 105, 30))
        self.ButTrans.setObjectName("ButTrans")
        self.InpVal = QtWidgets.QLineEdit(self.centralwidget)
        self.InpVal.setGeometry(QtCore.QRect(230, 180, 113, 20))
        self.InpVal.setText("")
        self.InpVal.setObjectName("InpVal")
        self.Home = QtWidgets.QPushButton(self.centralwidget)
        self.Home.setGeometry(QtCore.QRect(490, 10, 75, 23))
        self.Home.setObjectName("Home")
        self.destino = QtWidgets.QLabel(self.centralwidget)
        self.destino.setGeometry(QtCore.QRect(160, 220, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.destino.setFont(font)
        self.destino.setObjectName("destino")
        self.InpDest = QtWidgets.QLineEdit(self.centralwidget)
        self.InpDest.setGeometry(QtCore.QRect(230, 220, 113, 20))
        self.InpDest.setText("")
        self.InpDest.setObjectName("InpDest")
        self.label = QtWidgets.QLabel(self.centralwidget)
        #self.label.setGeometry(QtCore.QRect(160, 150, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        #self.label.setFont(font)
        #self.label.setObjectName("label")
        #self.InpNum = QtWidgets.QLineEdit(self.centralwidget)
        #self.InpNum.setGeometry(QtCore.QRect(230, 150, 113, 20))
        #self.InpNum.setText("")
        #self.InpNum.setObjectName("InpNum")
        Tela_transferen.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Tela_transferen)
        self.statusbar.setObjectName("statusbar")
        Tela_transferen.setStatusBar(self.statusbar)

        self.retranslateUi(Tela_transferen)
        QtCore.QMetaObject.connectSlotsByName(Tela_transferen)

    def retranslateUi(self, Tela_transferen):
        _translate = QtCore.QCoreApplication.translate
        Tela_transferen.setWindowTitle(_translate("Tela_transferen", "MainWindow"))
        self.Valor.setText(_translate("Tela_transferen", "Valor:"))
        self.Transfe.setText(_translate("Tela_transferen", "Transfer??ncia"))
        self.ButTrans.setText(_translate("Tela_transferen", "Transferir"))
        self.Home.setText(_translate("Tela_transferen", "Voltar"))
        self.destino.setText(_translate("Tela_transferen", "Destino:"))
        self.label.setText(_translate("Tela_transferen", "Numero:"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tela_transferen()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())