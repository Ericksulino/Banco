from datetime import datetime

class Historico:

    def init(self):
        self._historico = []

    def adicionar_transacao(cnta:str,transacao:str,cursor)->None:

        cursor.execute('INSERT INTO historico(numero_conta,transacoes) VALUES (%s,%s)',(cnta,transacao))

    def imprimir_transacoes(cnta:str,cursor)-> list:
        data_abertura = datetime.now().strftime('%d/%m/%Y %H:%M')
        historico = list(cursor.execute('SELECT transacoes FROM historico WHERE numero_conta = %s',(cnta)))
        h = []
        h.append("Conta aberta em: {}".format(data_abertura))
        h.append("Transações:")
        for i in historico:
            h.append(list(i)[0])
        return '\n'.join(h)
