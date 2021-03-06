
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QMainWindow,QApplication,QFileDialog
from PyQt5.QtCore import QCoreApplication
import socket
import os

ip = 'localhost'
porta = 8004
endereco = ((ip,porta))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(endereco)

#from conta import Conta
#from cliente import Cliente
#from banco import Banco

from tela_abrir_conta import Tela_Abrir_conta
from tela_home import Tela_Home
from tela_menu_cliente import Menu_Cliente
from tela_extrato import Tela_extrato
from tela_saque import Tela_saque
from tela_transferen import Tela_transferen
from tela_cadastro_cliente import Tela_Cadastro_Cliente
from tela_menu_conta import Tela_Menu_Conta
from tela_login import Tela_Login
from tela_acesso import Tela_Acesso
from tela_historico import Tela_Historico
from tela_busca_cliente import Tela_Busca_Cliente
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

        self.tela_histo.ButHome.clicked.connect(self.abrirMenuConta)
        

    def botaoCadastClie(self):
        nome = self.tela_cadsClie.lineEdit.text()
        cpf = self.tela_cadsClie.lineEdit_2.text()
        nascimento = self.tela_cadsClie.lineEdit_3.text()

        if not(nome == '' or cpf == '' or nascimento == ''):
            client_socket.send('add_cliente,{},{},{}'.format(nome,cpf,nascimento).encode())
            res = client_socket.recv(1024).decode()
    
            if(res == 'sucesso'):
                QMessageBox.information(None,'Banco','Cadastro realizado com sucesso!')
                self.tela_cadsClie.lineEdit.setText('')
                self.tela_cadsClie.lineEdit_2.setText('')
                self.tela_cadsClie.lineEdit_3.setText('')
            else:
                QMessageBox.information(None,'Banco','O CPF informado j?? se encontra cadastrado!')
        else:
            QMessageBox.information(None,'Banco','Todos os campos devem ser preeecidos!')
        self.abrirHome()

    
    def botaoCadastConta(self):
        num = self.tela_abrirConta.lineEdit.text()
        titular = self.tela_abrirConta.lineEdit_2.text()
        saldo = float(self.tela_abrirConta.lineEdit_3.text())
        limite = float(self.tela_abrirConta.lineEdit_4.text())
        
        client_socket.send('add_conta,{},{},{},{}'.format(num,titular,saldo,limite).encode())
        cnt = client_socket.recv(1024).decode()
        if not(num == '' or titular == '' or saldo == '' or limite == ''):

            if cnt == 'sucesso':
                
                QMessageBox.information(None,'Banco','Conta aberta com sucesso com sucesso!')
                self.tela_abrirConta.lineEdit.setText('')
                self.tela_abrirConta.lineEdit_2.setText('')
                self.tela_abrirConta.lineEdit_3.setText('')
                self.tela_abrirConta.lineEdit_4.setText('')
            else:
                QMessageBox.information(None,'Banco','O numero de conta ja encontra-se cadastrado!')
            
        else:
            QMessageBox.information(None,'Banco','Todos os campos devem ser preeecidos!')
        self.abrirHome()

    def botaoAcessaConta(self):
        num = self.tela_acesso.InpNum.text()

        if not(num == ''):
            cnta = []
            client_socket.send('busca_cnta,{}'.format(num).encode())
            conta = client_socket.recv(1024).decode()
            
            if(conta != 'erro'):
                
                self.loginConta = num
                self.num = num
                self.abrirMenuConta()
            
            else:
                QMessageBox.information(None,'Banco','O numero da conta informado n??o existe!')
                self.tela_acesso.InpNum.setText('')

        else:
            QMessageBox.information(None,'Banco','Informe o numero da conta!')

    def botaoLogin(self):
        pes = []
        cpf = self.tela_login.lineEdit.text()
        client_socket.send('busc_clie,{}'.format(cpf).encode())
        pessoa = client_socket.recv(1024).decode()
        
        if pessoa != 'erro':
            pes = pessoa.split(',')
            self.loginClien = cpf
            self.abrirTelaAcess()
            
            self.tela_login.lineEdit.setText('')
        else:
            QMessageBox.information(None,'Banco','O CPF informado n??o se encontra cadastrado!')
    
    def botaoBusca(self):
        pes = []
        cpf = self.tela_busca_cliente.lineEdit.text()
        client_socket.send('busc_clie,{}'.format(cpf).encode())
        pessoa = client_socket.recv(1024).decode()
        
        pes = pessoa.split(',')
        if(pessoa != 'erro'):
            self.tela_busca_cliente.lineEdit_2.setText(pes[1])
            self.tela_busca_cliente.lineEdit_3.setText(pes[2])

        else:
            QMessageBox.information(None,'Banco','CPF n??o encontrado!')
            self.tela_busca_cliente.lineEdit.setText('')

    def botaoSaque(self):
        
        #verivicar se valor nao e zero
        valor = float(self.tela_saque.InpVal.text())
        client_socket.send('saque,{},{}'.format(self.loginConta,valor).encode())
        saq = client_socket.recv(1024).decode()
        
        if (saq == 'sucesso'):
            QMessageBox.information(None,'Banco','Saque realizado com sucesso!')
            self.tela_saque.InpVal.setText('')
            self.abrirMenuConta()
        else:
            QMessageBox.information(None,'Banco','N??o foi poss??vel realizar o saque!')
        
    
    def botaoDeposito(self):
        num = self.tela_deposito.InpNum.text()
        valor = float(self.tela_deposito.lineEdit.text())
        client_socket.send('deposita,{},{}'.format(num,valor).encode())
        dep = client_socket.recv(1024).decode()
        
        if dep=='sucesso':
                QMessageBox.information(None,'Banco','Deposito realizado com sucesso!')
                self.tela_deposito.InpNum.setText('')
                self.tela_deposito.lineEdit.setText('')
                self.abrirMenuConta()
        else:
            QMessageBox.information(None,'Banco','N??o foi poss??vel realizar o deposito!')

    def botaoTransfere(self):
        dest = []
        
        valor = float(self.tela_transf.InpVal.text())
        destino = self.tela_transf.InpDest.text()
        client_socket.send('busca_cnta,{}'.format(destino).encode())
        des = client_socket.recv(1024).decode()
        dest = des.split(',')
        if (des != 'erro'):
            client_socket.send('transfere,{},{},{}'.format(self.loginConta,valor,destino).encode())
            trans = client_socket.recv(1024).decode()
            if(trans == 'sucesso'):
                
                QMessageBox.information(None,'Banco','Transferencia executada!')
                
                self.tela_transf.InpVal.setText('')
                self.tela_transf.InpDest.setText('')
                self.abrirMenuConta
            else:
                QMessageBox.information(None,'Banco','Transferencia n??o executada!')
        else:
            QMessageBox.information(None,'Banco','Conta de destino n??o existe!')

    def botaoExtrato(self):
        '''num = self.tela_extrato.InpNum.text()
        tit = self.tela_extrato.OutTit.text()'''
        self.abrirTelaExtr()
        client_socket.send('saldo,{}'.format(self.loginConta).encode())
        extr = client_socket.recv(1024).decode()
        
        self.tela_extrato.OutSald.setText(extr)
        
    def botaoHistorico(self):
        self.abrirTelaHist()
        client_socket.send('historic,{}'.format(self.loginConta).encode())
        hist = client_socket.recv(1024).decode()
       
        self.tela_histo.textEdit.setText(hist)
    
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
    import sys
    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    show_main = Main()
    sys.exit(app.exec_())

client_socket.close()