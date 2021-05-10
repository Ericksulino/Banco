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

class Ui_Main(QtWidgets.QWidget):
