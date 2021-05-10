import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QMainWindow,QApplication,QFileDialog
from PyQt5.QtCore import QCoreApplication

from conta import Conta
from cliente import Cliente
from banco import Banco

from abrirConta import Tela_Abrir_conta
from home import Tela_Home
from menuCliente import Menu_Cliente
from tela_extrato import Tela_extrato
from tela_saque import Tela_saque
from tela_transferen import Tela_transferen
from cadastroCliente import Tela_Cadastro_Cliente

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640,480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()

        self.tela_inicio = Tela_Home()
        self.tela_inicio.setupUi(self.stack0)

        self.tela_abrirConta = Tela_Abrir_conta()
        self.tela_abrirConta.setupUi(self.stack1)

        self.tela_cadsClie = Tela_Cadastro_Cliente()
        self.tela_cadsClie.setupUi(self.stack2)

        self.tela_saque = Tela_saque()
        self.tela_saque.setupUi(self.stack3)

        self.tela_extrato = Tela_extrato()
        self.tela_extrato.setupUi(self.stack4)

        self.tela_transf = Tela_transferen()
        self.tela_transf.setupUi(self.stack5)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
class Main(QMainWindow,Ui_Main):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)

        self.ban = Banco()
        self.tela_inicio.ButCliente.clicked.connect(self.abrirTelaCadClie)
        self.tela_inicio.ButConta.clicked.connect(self.abrirTelaConta)

    
    def abrirHome(self):
        self.QtStack.setCurrentIndex(0)

    def abrirTelaConta(self):
        self.QtStack.setCurrentIndex(1)

    def abrirTelaCadClie(self):
        self.QtStack.setCurrentIndex(2)
    
    def abrirTelaSaque(self):
        self.QtStack.setCurrentIndex(3)
    
    def abrirTelaExtr(self):
        self.QtStack.setCurrentIndex(4)
    
    def abrirTelaTransf(self):
        self.QtStack.setCurrentIndex(5)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    show_main = Main()
    sys.exit(app.exec_())