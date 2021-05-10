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
from tela_menu_conta import Tela_Menu_Conta
from tela_login import Tela_Login
from tela_acesso import Tela_Acesso

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
        self.stack6 = QtWidgets.QMainWindow()
        self.stack7 = QtWidgets.QMainWindow()
        self.stack8 = QtWidgets.QMainWindow()
        self.stack9 = QtWidgets.QMainWindow()

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

        self.tela_menu_clie = Menu_Cliente()
        self.tela_menu_clie.setupUi(self.stack6)

        self.tela_login = Tela_Login()
        self.tela_login.setupUi(self.stack7)

        self.tela_menu_conta = Tela_Menu_Conta()
        self.tela_menu_conta.setupUi(self.stack8)

        self.tela_acesso = Tela_Acesso()
        self.tela_acesso.setupUi(self.stack9)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)
        self.QtStack.addWidget(self.stack8)
        self.QtStack.addWidget(self.stack9)

class Main(QMainWindow,Ui_Main):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)

        self.ban = Banco()
        self.tela_inicio.ButCliente.clicked.connect(self.abrirMenuClie)
        self.tela_inicio.ButConta.clicked.connect(self.abrirTelaLog)

        self.tela_login.ButCadas.clicked.connect(self.abrirTelaConta)
        self.tela_login.ButHome.clicked.connect(self.abrirHome)
        self.tela_login.ButLogin.clicked.connect(self.conta)

        self.tela_menu_clie.ButCadastrar.clicked.connect(self.abrirTelaCadClie)
        self.tela_menu_clie.ButHome.clicked.connect(self.abrirHome)

        self.tela_cadsClie.ButCadastrar.clicked.connect(self.botaoCadastClie)
        self.tela_cadsClie.ButHome.clicked.connect(self.abrirHome)

        
    
    def botaoCadastClie(self):
        nome = self.tela_cadsClie.lineEdit.text()
        cpf = self.tela_cadsClie.lineEdit_2.text()
        nascimento = self.tela_cadsClie.lineEdit_3.text()
        if not(nome == '' or cpf == '' or nascimento == ''):
            p = Cliente(nome,cpf,nascimento)
            if(self.ban.adicionar_cliente(p)):
                QMessageBox.information(None,'Banco','Cadastro realizado com sucesso!')
                self.tela_cadsClie.lineEdit.setText('')
                self.tela_cadsClie.lineEdit_2.setText('')
                self.tela_cadsClie.lineEdit_3.setText('')
            else:
                QMessageBox.information(None,'Banco','O CPF informado já se encontra cadastrado!')
        else:
            QMessageBox.information(None,'Banco','Todos os campos devem ser preeecidos!')
        self.abrirHome()
    '''
    def botaoCadastConta(self):
        num = self.tela_cadsClie.lineEdit.text()
        cpf = self.tela_cadsClie.lineEdit_2.text()
        nascimento = self.tela_cadsClie.lineEdit_3.text()
        if not(nome == '' or cpf == '' or nascimento == ''):
            p = Cliente(nome,cpf,nascimento)
            if(self.ban.adicionar_cliente(p)):
                QMessageBox.information(None,'Banco','Cadastro realizado com sucesso!')
                self.tela_cadsClie.lineEdit.setText('')
                self.tela_cadsClie.lineEdit_2.setText('')
                self.tela_cadsClie.lineEdit_3.setText('')
            else:
                QMessageBox.information(None,'Banco','O CPF informado já se encontra cadastrado!')
        else:
            QMessageBox.information(None,'Banco','Todos os campos devem ser preeecidos!')
        self.abrirHome()
'''
    def conta(self):
        cpf = self.tela_login.lineEdit.text()
        pessoa = self.ban.busca_clie(cpf)
        if pessoa != None:
            self.abrirTelaAcess()
            self.tela_acesso.OutNom.setText(pessoa.nome)
        else:
            QMessageBox.information(None,'Banco','O CPF informado não se encontra cadastrado!')
            
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
    
    def abrirMenuClie(self):
        self.QtStack.setCurrentIndex(6)
    
    def abrirTelaLog(self):
        self.QtStack.setCurrentIndex(7)
    
    def abrirMenuConta(self):
        self.QtStack.setCurrentIndex(8)
    
    def abrirTelaAcess(self):
        self.QtStack.setCurrentIndex(9)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    show_main = Main()
    sys.exit(app.exec_())