from historico import Historico
from datetime import datetime
from pessoa import Cliente

class Conta:

    saldo_atualizado = "UPDATE contas SET saldo = %d WHERE id = ?"

    def __init__(self,numero:str,titular:str,saldo:float,limite:float):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
        self._data_abertura = str(datetime.now().strftime('%d/%m/%Y %H:%M'))
        self._historico = Historico()

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
    def abrir_conta(num,tit,sald,lim,cursor,sinc):

        if (Conta.busca_conta(num,cursor,sinc)) == False:
            cursor.execute("INSERT INTO contas(numero,titular,saldo,limite) VALUES (%s,%s,%s,%s)",(num,tit,sald,lim))
            return True
        else:
            return False
    
    #Pronto
    def saca(cnta:str,valor:float,cursor,controle)->bool:

        saldo = 0.0

        cursor.execute('SELECT numero,saldo FROM contas')
        for conta in cursor:
            conta[0] == cnta
            saldo = conta[1]

        if valor <= saldo and valor > 0:
            saldo -= valor
            cursor.execute('UPDATE contas SET saldo = %s WHERE numero = %s',(float(saldo),cnta))

            if controle:
                nova_transacao = 'Saque -- Data: {} Valor: {}'.format((datetime.now().strftime('%d/%m/%Y %H:%M')),valor)
                Historico.adicionar_transacao(cnta,nova_transacao,cursor)
            return True
        return False

    def deposita(cnta:str,valor:float,cursor,controle,sinc)->bool:

        saldo = 0.0
        sinc.acquire()
        cursor.execute('SELECT numero,saldo FROM contas')
        sinc.release()
        for conta in cursor:
            conta[0] == cnta
            saldo = conta[1]

            if valor > 0:
                saldo += valor
                sinc.acquire()
                cursor.execute('UPDATE contas SET saldo = %s WHERE numero = %s',(float(saldo),cnta))
                sinc.release()

            if controle:
                nova_transacao = 'Deposito -- Data: {} Valor: {}'.format(datetime.now().strftime('%d/%m/%Y %H:%M'),valor)
                Historico.adicionar_transacao(cnta,nova_transacao,cursor,sinc)
            return True
        return False

    def transfere(cnta:str,valor:float,destino:str,cursor)->bool:

        if Conta.saca(cnta,valor,cursor,False):
 
            if Conta.deposita(destino,valor,cursor,False):

                cursor.execute('SELECT titular,numero FROM contas')
                for num_cont in cursor:
                    if(num_cont[1] == destino):
                        aux = num_cont[0]
                
                cursor.execute('SELECT nome,cpf FROM pessoas')
                for nome in cursor:
                    if(nome[1] == aux):
                        cliente = nome[0]

                nova_transacao = 'Transferencia para {} -- Data: {} Valor: {}'.format(cliente,datetime.now().strftime('%d/%m/%Y %H:%M'),valor)
                Historico.adicionar_transacao(cnta,nova_transacao,cursor)
                
                cursor.execute('SELECT titular,numero FROM contas')
                for num_cont2 in cursor:
                    if(num_cont2[1] == cnta):
                        aux2 = num_cont2[0]
                
                cursor.execute('SELECT nome,cpf FROM pessoas')
                for nome2 in cursor:
                    if(nome2[1] == aux):
                        cliente2 = nome2[0]

                nova_transacao = 'Tranferencia recebida de "{}" -- Data: {} Valor: {} '.format(cliente2,datetime.now().strftime('%d/%m/%Y %H:%M'),valor)
                Historico.adicionar_transacao(destino,nova_transacao,cursor)

                return True
        return False

    #Pronto
    def busca_conta(numero_bus:str,cursor,sinc):

        sinc.acquire()
        cursor.execute('SELECT numero FROM contas')
        sinc.release()
        
        for conta in cursor:
            if (conta[0] == numero_bus):
                return True
        return False

    def ver_historico(self):
        return self.historico.imprimir_transacoes()

    def extrato(cnta:str,cursor):

        cursor.execute('SELECT numero,saldo FROM contas')
        for conta in cursor:
            if(conta[0] == cnta):
                return conta[1]
        return False