import datetime

class Historico:

    def init(self):
        self._historico = []

        '''self._data_abertura = datetime.datetime.today()
        self._transacoes = "Conta aberta em: {}\n Transações:\n".format(self._data_abertura)'''

    def adicionar_transacao(transacao:str,cursor):
        #self._transacoes +=trans
        cursor.execute("INSERT INTO historico (transacoes) VALUES (?)",(transacao))

    def imprimir_transacoes(titular:str,cursor)-> list:
        historico = list(cursor.execute("SELECT transacoes FROM historico = {}".format(titular)))
        h = []
        for i in historico:
            h.append(list(i)[0])
        return h
        #return self._transacoes
