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
        if not(Conta.busca_conta(num,cursor)):
            cursor.execute("INSERT INTO contas(numero,titular,saldo,limite) VALUES (?,?,?,?)",(num,tit,sald,lim))
            return True
        else:
            return False

    '''def deposita(self, valor):
        if valor+self._saldo<=self.limite:
            self._saldo+=valor
            self.historico.adicionar_transacao(" - Depositou: {}\n".format(valor))
            return True
        else: return False'''
    
    #Pronto
    def saca(cnta:str,valor:float,cursor,controle)->bool:

        saldo = list(cursor.execute('SELECT saldo FROM contas WHERE numero = "{}"'.format(cnta)))[0][0]
        if valor <= saldo and valor > 0:
            saldo -= valor
            cursor.execute('UPDATE contas SET saldo = "{}" WHERE numero = "{}"'.format(saldo,cnta))
            
            #titular = list(cursor.execute('SELECT titular FROM contas WHERE numero = "{}"'.format(cnta)))[0][0]
            if controle:
                nova_transacao = 'Saque -- Data: "{}" Valor: "{}"\n'.format((datetime.now().strftime('%d/%m/%Y %H:%M')),valor)
                Historico.adicionar_transacao(cnta,nova_transacao,cursor)
            return True
        return False

    def deposita(cnta:str,valor:float,cursor,controle)->bool:
        saldo = list(cursor.execute('SELECT saldo FROM contas WHERE numero = "{}"'.format(cnta)))[0][0]
        if valor > 0:
            saldo += valor
            cursor.execute('UPDATE contas SET saldo = "{}" WHERE numero = "{}"'.format(saldo,cnta))
            if controle:
                nova_transacao = 'Deposito -- Data: "{}" Valor: "{}"'.format(datetime.now().strftime('%d/%m/%Y %H:%M'),valor)
                Historico.adicionar_transacao(cnta,nova_transacao,cursor)
            return True
        return False

    def transfere(cnta:str,valor:float,destino:str,cursor)->bool:
        if Conta.saca(cnta,valor,cursor,False):

            if Conta.deposita(destino,valor,cursor,False):

                aux = list(cursor.execute('SELECT titular FROM contas WHERE numero = "{}"'.format(destino)))[0][0]
                cliente = list(cursor.execute('SELECT nome FROM pessoas WHERE cpf = "{}"'.format(aux)))[0][0]

                nova_transacao = 'Transferencia para "{}" -- Data: "{}" Valor: "{}" \n'.format(cliente,datetime.now().strftime('%d/%m/%Y %H:%M'),valor)
                Historico.adicionar_transacao(cnta,nova_transacao,cursor)
                
                aux2 = list(cursor.execute('SELECT titular FROM contas WHERE numero = "{}"'.format(cnta)))[0][0]
                cliente2 = list(cursor.execute('SELECT nome FROM pessoas WHERE cpf = "{}"'.format(aux2)))[0][0]
                
                nova_transacao = 'Tranferencia recebida de "{}" -- Data: "{}" Valor: "{}" \n'.format(cliente2,datetime.now().strftime('%d/%m/%Y %H:%M'),valor)
                Historico.adicionar_transacao(destino,nova_transacao,cursor)

                return True
        return False

    #Pronto
    def busca_conta(numero_bus:str,cursor):

        busca = 'SELECT numero FROM contas WHERE numero = "{}"'.format(numero_bus)
        cnt = list(cursor.execute(busca))

        if(len(cnt)!=0):
            return True
        return False

    def ver_historico(self):
        return self.historico.imprimir_transacoes()

    def extrato(cnta:str,cursor):
        return list(cursor.execute('SELECT saldo FROM contas WHERE numero = "{}"'.format(cnta)))[0][0]