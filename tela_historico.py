# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'histórico.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_Historico(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.OutHist = QtWidgets.QLineEdit(self.centralwidget)
        self.OutHist.setGeometry(QtCore.QRect(120, 80, 441, 351))
        self.OutHist.setObjectName("OutHist")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 40, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ButHome = QtWidgets.QPushButton(self.centralwidget)
        self.ButHome.setGeometry(QtCore.QRect(510, 20, 75, 23))
        self.ButHome.setObjectName("ButHome")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Histórico"))
        self.ButHome.setText(_translate("MainWindow", "HOME"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tela_Historico()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())