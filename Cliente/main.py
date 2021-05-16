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
from tela_historico import Tela_Historico
from telaBuscaClie import Tela_Busca_Cliente
from tela_deposito import Tela_Deposito

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
        self.stack10 = QtWidgets.QMainWindow()
        self.stack11 = QtWidgets.QMainWindow()
        self.stack12 = QtWidgets.QMainWindow()

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

        self.tela_histo = Tela_Historico()
        self.tela_histo.setupUi(self.stack10)

        self.tela_busca_cliente = Tela_Busca_Cliente()
        self.tela_busca_cliente.setupUi(self.stack11)

        self.tela_deposito = Tela_Deposito()
        self.tela_deposito.setupUi(self.stack12)

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
        self.QtStack.addWidget(self.stack10)
        self.QtStack.addWidget(self.stack11)
        self.QtStack.addWidget(self.stack12)

class Main(QMainWindow,Ui_Main):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)

        self.ban = Banco()
        self.loginConta = None
        self.loginClien = None
        self.tela_inicio.ButCliente.clicked.connect(self.abrirMenuClie)
        self.tela_inicio.ButConta.clicked.connect(self.abrirTelaLog)

        self.tela_login.ButCadas.clicked.connect(self.abrirTelaConta)
        self.tela_login.ButHome.clicked.connect(self.abrirHome)
        self.tela_login.ButLogin.clicked.connect(self.botaoLogin)

        self.tela_menu_clie.ButCadastrar.clicked.connect(self.abrirTelaCadClie)
        self.tela_menu_clie.ButHome.clicked.connect(self.abrirHome)

        self.tela_cadsClie.ButCadastrar.clicked.connect(self.botaoCadastClie)
        self.tela_cadsClie.ButHome.clicked.connect(self.abrirHome)

        self.tela_abrirConta.ButCadastar.clicked.connect(self.botaoCadastConta)
        self.tela_abrirConta.ButHome.clicked.connect(self.abrirHome)

        self.tela_acesso.ButAcess.clicked.connect(self.botaoAcessaConta)
        self.tela_acesso.ButHome.clicked.connect(self.botaoLogoutClie)

        self.tela_menu_conta.ButSaq.clicked.connect(self.abrirTelaSaque)
        self.tela_menu_conta.ButDep.clicked.connect(self.abrirDeposito)
        self.tela_menu_conta.pushButton_4.clicked.connect(self.abrirTelaHist)
        self.tela_menu_conta.ButTrans.clicked.connect(self.abrirTelaTransf)
        self.tela_menu_conta.ButSald.clicked.connect(self.botaoExtrato)
        self.tela_menu_conta.pushButton_4.clicked.connect(self.botaoHistorico)
        self.tela_menu_conta.ButHome.clicked.connect(self.botaoLogoutCont)

        self.tela_menu_clie.ButBuscar.clicked.connect(self.abrirBusca)

        self.tela_busca_cliente.butBuscar.clicked.connect(self.botaoBusca)
        self.tela_busca_cliente.butHome.clicked.connect(self.abrirHome)

        self.tela_saque.ButSaque.clicked.connect(self.botaoSaque)
        self.tela_saque.Home.clicked.connect(self.abrirMenuConta)

        self.tela_deposito.pushButton.clicked.connect(self.botaoDeposito)
        self.tela_deposito.ButHome.clicked.connect(self.abrirMenuConta)

        self.tela_transf.ButTrans.clicked.connect(self.botaoTransfere)
        self.tela_transf.Home.clicked.connect(self.abrirMenuConta)

        self.tela_extrato.Home.clicked.connect(self.abrirMenuConta)
        #self.tela_extrato.ButExtr.clicked.connect(self.botaoExtrato)

        self.tela_histo.ButHome.clicked.connect(self.abrirMenuConta)
        


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

    
    def botaoCadastConta(self):
        num = self.tela_abrirConta.lineEdit.text()
        titular = self.tela_abrirConta.lineEdit_2.text()
        saldo = float(self.tela_abrirConta.lineEdit_3.text())
        limite = float(self.tela_abrirConta.lineEdit_4.text())
        pessoa = self.ban.busca_clie(titular)
        if not(num == '' or titular == '' or saldo == '' or limite == ''):
            if pessoa != None:
                c = Conta(num,pessoa,saldo,limite)
                if(self.ban.adcionar_conta(c)):
                    QMessageBox.information(None,'Banco','Conta aberta com sucesso com sucesso!')
                    self.tela_abrirConta.lineEdit.setText('')
                    self.tela_abrirConta.lineEdit_2.setText('')
                    self.tela_abrirConta.lineEdit_3.setText('')
                    self.tela_abrirConta.lineEdit_4.setText('')
                else:
                    QMessageBox.information(None,'Banco','O numero de conta ja encontra-se cadastrado!')
            else:
                QMessageBox.information(None,'Banco','Pessoa não cadastrada!')
        else:
            QMessageBox.information(None,'Banco','Todos os campos devem ser preeecidos!')
        self.abrirHome()

    def botaoAcessaConta(self):
        num = self.tela_acesso.InpNum.text()

        if not(num == ''):
            existe = self.ban.busca_conta(num)
            if(existe != None):
                if(existe.titular.cpf == self.loginClien.cpf):
                    self.loginConta = existe
                    self.num = num
                    self.abrirMenuConta()
                else:
                   QMessageBox.information(None,'Banco','O numero da conta informado não está atrelado a esse CPF!') 
            else:
                QMessageBox.information(None,'Banco','O numero da conta informado não existe!')
                self.tela_acesso.InpNum.setText('')

        else:
            QMessageBox.information(None,'Banco','Informe o numero da conta!')

    def botaoLogin(self):
        cpf = self.tela_login.lineEdit.text()
        pessoa = self.ban.busca_clie(cpf)
        if pessoa != None:
            self.loginClien = pessoa
            self.abrirTelaAcess()
            self.tela_acesso.OutNom.setText(pessoa.nome)
            self.tela_login.lineEdit.setText('')
        else:
            QMessageBox.information(None,'Banco','O CPF informado não se encontra cadastrado!')
    
    def botaoBusca(self):
        cpf = self.tela_busca_cliente.lineEdit.text()
        pessoa = self.ban.busca_clie(cpf)
        if(pessoa != None):
            self.tela_busca_cliente.lineEdit_2.setText(pessoa.nome)
            self.tela_busca_cliente.lineEdit_3.setText(pessoa.data_nascimento)

        else:
            QMessageBox.information(None,'Banco','CPF não encontrado!')
            self.tela_busca_cliente.lineEdit.setText('')

    def botaoSaque(self):
        #num = self.tela_saque.InpNum.text()
        valor = float(self.tela_saque.InpVal.text())
        saq = self.loginConta.saca(valor)
        if saq:
            QMessageBox.information(None,'Banco','Saque realizado com sucesso!')
            self.tela_acesso.InpNum.setText('')
            self.abrirMenuConta
        else:
            QMessageBox.information(None,'Banco','Não foi possível realizar o saque!')
        
    
    def botaoDeposito(self):
        num = self.tela_deposito.InpNum.text()
        valor = float(self.tela_deposito.lineEdit.text())
        dep = self.ban.deposita(num,valor)
        if dep:
                QMessageBox.information(None,'Banco','Deposito realizado com sucesso!')
                self.tela_acesso.InpNum.setText('')
                self.abrirMenuConta
        else:
                QMessageBox.information(None,'Banco','Não foi possível realizar o deposito!')

    def botaoTransfere(self):
        #num = self.tela_transf.InpNum.text()
        valor = float(self.tela_transf.InpVal.text())
        destino = self.tela_transf.InpDest.text()

        if (self.ban.busca_conta(destino) != None):
            self.loginConta.transfere(valor,destino)
            QMessageBox.information(None,'Banco','Transferencia executada!')
            self.tela_transf.InpNum.setText('')
            self.tela_transf.InpVal.setText('')
            self.tela_transf.InpDest.setText('')
            self.abrirMenuConta
        else:
            QMessageBox.information(None,'Banco','Conta de destino não existe!')

    def botaoExtrato(self):
        '''num = self.tela_extrato.InpNum.text()
        tit = self.tela_extrato.OutTit.text()'''
        self.abrirTelaExtr()
        extr = str(self.loginConta.extrato())
        #if(self.loginConta!=None):
        self.tela_extrato.OutTit.setText(self.loginConta.titular.nome)
        self.tela_extrato.OutSald.setText(extr)
        #else:
        #QMessageBox.information(None,'Banco','Conta não encontrada!')

    def botaoHistorico(self):
        self.abrirTelaHist()
        x = self.loginConta.ver_historico()
        self.tela_histo.textEdit.setText(x)
    
    def botaoLogoutCont(self):
        self.loginConta = None
        self.abrirTelaAcess()
    
    def botaoLogoutClie(self):
        self.loginClien = None
        self.abrirTelaLog()

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
    
    def abrirTelaHist(self):
        self.QtStack.setCurrentIndex(10)

    def abrirBusca(self):
        self.QtStack.setCurrentIndex(11)
    
    def abrirDeposito(self):
        self.QtStack.setCurrentIndex(12)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    show_main = Main()
    sys.exit(app.exec_())