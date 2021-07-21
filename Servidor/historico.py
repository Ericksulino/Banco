from datetime import datetime

class Historico:

    def init(self):
        self._historico = []

    def adicionar_transacao(cnta:str,transacao:str,cursor)->None:

        cursor.execute('INSERT INTO historico(numero_conta,transacoes) VALUES (%s,%s)',(cnta,transacao))

    def imprimir_transacoes(cnta:str,cursor)-> list:
        h = []
        
        data_abertura = datetime.now().strftime('%d/%m/%Y %H:%M')
        
        cursor.execute('SELECT numero_conta,transacoes FROM historico')

        h.append("Conta aberta em: {}".format(data_abertura))
        h.append("Transações:")

        for transacao in cursor:
            if(str(transacao[0])==cnta):
                h.append(transacao[1])
        if len(h) == 0:
            h.append('')
        return h
        
