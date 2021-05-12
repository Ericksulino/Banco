import datetime

class Historico:

    def __init__(self):
        self._data_abertura = datetime.datetime.today()
        self._transacoes = "Conta aberta em: {}\n Transações:\n".format(self._data_abertura)

    def adicionar_transacao(self, trans):
        self._transacoes +=trans

    def imprimir_transacoes(self):
        return self._transacoes
