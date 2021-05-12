import datetime

class Historico:

    def __init__(self):
        self._data_abertura = datetime.datetime.today()
        self._transacoes = []

    def adicionar_transacao(self, str):
        self._transacoes.append(str)

    def imprimir_transacoes(self):
        print("Conta aberta em: ", self._data_abertura)
        print("Transações:")
        i = ''
        for t in self._transacoes:
            i = i + '\n' + t
            print(t)

        return i
