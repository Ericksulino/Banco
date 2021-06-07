import datetime

class Historico:

    def init(self):
        self._historico = []

        '''self._data_abertura = datetime.datetime.today()
        self._transacoes = "Conta aberta em: {}\n Transações:\n".format(self._data_abertura)'''

    def adicionar_transacao(titular:str,valor:str,cursor):
        #self._transacoes +=trans
        cursor.execute("ISERT INTO historico(titular,transacoes) VALUES (?,?)",(titular,valor))

    def imprimir_transacoes(titular:str,cursor)-> list:
        historico = list(cursor.execute("SELECT transacoes FROM historico WHERE titular = {}".format(titular)))
        h = []
        for i in historico:
            h.append(list(i)[0])
        return h
        #return self._transacoes
