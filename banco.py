from cliente import Cliente
from conta import Conta

class Banco:
    def __init__(self):
        self._lista_clie = {}
        self._lista_contas = {}

    def busca_conta(self,num):
        if num in self._lista_contas:
            return self._lista_contas[num]
        else:
            return None
    
    def busca_clie(self,cpf):
        if cpf in self._lista_clie:
            return self._lista_clie[cpf]
        else:
            return None

    def adcionar_conta(self,cnta):
        if self.busca_conta(cnta.numero) != None:
            return False
        else:
            self._lista_contas[cnta.numero] = cnta
            return True
    
    def adicionar_cliente(self,clie):
        if self.busca_clie(clie.cpf) != None:
            return False
        else:
            self._lista_clie[clie.cpf] = clie
            return True

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
    
                
        