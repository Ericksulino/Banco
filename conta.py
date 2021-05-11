from historico import Historico
class Conta():

    _total_contas = 0

    __slots__ = ['_numero','_titular','_saldo','_limite','_historico']
    def __init__(self,numero,titular,saldo,limite = 1000.0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
        self._historico = Historico()
        Conta._total_contas+=1

    @staticmethod
    def get_total_contas():
        return Conta._total_contas

    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self,num):
        self._numero = num
    
    @property
    def titular(self):
        return self._titular
    
    @titular.setter
    def cpf_do_titular(self,tit):
        self._titular = tit
    
    @property
    def limite(self):
        return self._limite
    
    @limite.setter
    def limite(self,lim):
        self._limite = lim

    @property
    def historico(self):
        return self._historico
    
    @historico.setter
    def historico(self,hist):
        self._historico = hist

    def deposita(self, valor):
        if valor+self._saldo<=self.limite:
            self._saldo+=valor
            self.historico.adicionar_transacao(f" - Depositou: {valor}")
            return True
        else: return False
    
    def saca(self, valor):
        if valor<=self._saldo:
            self._saldo-=valor
            self.historico.adicionar_transacao(f" - Sacou: {valor}")
            return True
        else: return False
    
    def transfere(self,valor,destino):
        retirar = self.saca(valor)
        if retirar == False:
            return False
        else:
            destino.deposita(valor)
            self.historico.adicionar_transacao(f" - Transferiu {valor} para {destino.titular.nome}")
            return True

    def ver_historico(self):
        self.historico.imprimir_transacoes()

    def extrato(self):
        return self._saldo