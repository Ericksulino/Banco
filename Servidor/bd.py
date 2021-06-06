from pessoa import Cliente
from conta import Conta
import sqlite3

conexao = sqlite3.connect('teste.sqlite')
cursor = conexao.cursor()

class Banco:
    def __init__(self):
        #self._lista_clie = []
        #self._lista_contas = []
        sql = """CREATE TABLE IF NOT EXISTS clientes(nome text NOT NULL, cpf text NOT NULL, data_nascimento text NOT NULL);"""
        sql2 = """CREATE TABLE IF NOT EXISTS contas(numero integer NOT NULL, titular text NOT NULL,saldo integer,limite integer, historico text);"""

        cursor.execute(sql)
        cursor.execute(sql2)

    def busca_conta(self,num):
        cursor.execute('SELECT * FROM cntas WHERE numero == (?)',(num))
        '''for lp in self._lista_contas:
            if lp.numero == num:
                return lp'''

        return None
    
    def busca_clie(self,cpf):
        for lp in self._lista_clie:
            if lp.cpf == cpf:
                return lp

        return None

    def adcionar_conta(self,cnta):
        existe = self.busca_conta(cnta.numero)
        if (existe == None):
            self._lista_contas.append(cnta)
            return True

        else:
            return False
    
    def adicionar_cliente(self,clie):
        existe = self.busca_clie(clie.cpf)
        if (existe == None):
            self._lista_clie.append(clie)
            return True

        else:
            return False

    def transfere(self,num,valor,numDest):
        rem = self.busca_conta(num)
        dest = self.busca_conta(numDest)
        if rem != None:
            if dest != None:
                if (rem.transfere(valor,dest)):
                    return True
                else:
                    return False
            else: 
                return False
        else:
            return False
    
    def saque(self,num,valor):
        cnta = self.busca_conta(num)
        if cnta != None:
            saq = cnta.saca(valor)
            return saq
        else:
            return False

    def deposita(self,num,valor):
        cnta = self.busca_conta(num)
        if cnta != None:
            dep = cnta.deposita(valor)
            return dep
        else:
            return False
    
    def extrato(self,num):
        cnta = self.busca_conta(num)
        if cnta == None:
            return None
        else:
            extr = cnta.extrato()
            return extr


    def historico(self,num):
        cnta = self.busca_conta(num)
        if cnta == None:
            return None
        else:
            hist = cnta.ver_historico()
            return hist
            
                
ban = Banco()
