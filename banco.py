from cliente import Cliente
from conta import Conta

class Banco:
    def __init__(self):
        self._lista_clie = []
        self._lista_contas = []

    def busca_conta(self,num):
        for lp in self._lista_contas:
            if lp.numero == num:
                return lp

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

    def transfere(self,num,numDest,valor):
        if self.busca_conta(num) != None:
            if self.busca_conta(numDest) != None:
                if (self._lista_contas[num].transfere(valor,self._lista_contas[numDest])):
                    return True
                else:
                    return False
            else: 
                return False
        else:
            return False
    
    def saque(self,num,valor):
        if self.busca_conta(num) != None:
            saq = self._lista_contas[num].saca(valor)
            return saq
        else:
            return False

    def deposita(self,num,valor):
        if self.busca_conta(num) != None:
            saq = self._lista_contas[num].deposita(valor)
            return saq
        else:
            return False
                
        