from historico import Historico
from datetime import datetime
from pessoa import Cliente

class Conta:

    #_total_contas = 0

    #__slots__ = ['_numero','_titular','_saldo','_limite','_historico']

    saldo_atualizado = "UPDATE contas SET saldo = ? WHERE id = ?"

    def __init__(self,numero:str,titular:str,saldo:float,limite:float):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
        self._data_abertura = str(datetime.now().strftime('%d/%m/%Y %H:%M'))
        self._historico = Historico()
        #Conta._total_contas+=1

    '''@staticmethod
    def get_total_contas():
        return Conta._total_contas'''

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

    #Pronto
    def abrir_conta(num,tit,sald,lim,cursor):
        cursor.execute("INSERT INTO contas(numero,titular,saldo,limite) VALUES (?,?,?)",(num,tit,sald,lim)
        return conta._numero

    '''def deposita(self, valor):
        if valor+self._saldo<=self.limite:
            self._saldo+=valor
            self.historico.adicionar_transacao(" - Depositou: {}\n".format(valor))
            return True
        else: return False'''
    
    #Pronto
    def saca(cnta, valor:float,cursor,controle)->bool:

        saldo = list(cursor.execute('SELECT saldo FROM contas WHERE id = "{}"'.format(cnta)))[0][0]
        if valor <= saldo and valor > 0:
            saldo -= valor
            cursor.execute('UPDATE contas SET saldo = "{}" WHERE id = "{}"'.format(saldo,cnta))
            if controle:
                nova_transacao = 'Saque -- Data: "{}" Valor: "{}"\n'.format(datetime.now().strftime('%d/%m/%Y %H:%M'),valor)
                Historico.adicionar_transacao(id_conta,nova_transacao,cursor)
            return True
        return False
        
    #Pronto
    def deposita(id_conta:str,valor:float,cursor,controle)->bool:
        saldo = list(cursor.execute("SELECT saldo FROM contas WHERE id = '{}'".format(id_conta)))[0][0]
        if valor > 0:
            saldo += valor
            cursor.execute('UPDATE contas SET saldo = ? WHERE id = ?;'.format(saldo,id_conta))
            if controle:
                nova_transacao = 'Deposito -- Data: {} Valor: {}'.format(datetime.now().strftime('%d/%m/%Y %H:%M'),valor)
                Historico.adicionar_transacao(id_conta,nova_transacao,cursor)
            return True
        return False

    def transfere(id_conta:int,valor:float,destino:str,cursor)->bool:
        if Conta.saca(id_conta,valor,cursor,False):

            id_cliente = list(cursor.execute('SELECT nome FROM pessoas Where id = {}'.format(destino)))[0][0]
            nome = list(cursor.execute('SELECT nome FROM pessoas WHERE id = {}'.format(id_cliente)))[0]
            nova_transacao = 'Transferencia para {} -- Data: {} Valor: {} \n'.format(datetime.now().strftime('%d/%m/%Y %H:%M'),valor)
            Historico.adicionar_transacao(id_conta,nova_transacao,cursor)

            id_cliente = list(cursor.execute('SELECT titular FROM contas WHERE id = {}'.format(id_conta)))[0][0]
            nome = list(cursor.execute('SELECT nome FROM pessoas WHERE id = {}'.format(id_cliente)))[0]

            nova_transacao = 'Tranferencia recebida de {} -- Data: {} Valor: {} \n'.format(datetime.now().strftime('%d/%m/%Y %H:%M'),valor)
            Historico.adicionar_transacao(destino,nova_transacao,cursor)

            return True
        return False

    #Pronto
    def busca_conta(numero_bus:str,cursor):

        busca = "SELECT * FROM contas WHERE numero = '{}'".format(numero_bus)
        cnt = list(cursor.execute(busca))

        if(len(cnt)!=0):
            return cnt[0][0]
        return False

    def ver_historico(self):
        return self.historico.imprimir_transacoes()

    def extrato(self):
        return self._saldo