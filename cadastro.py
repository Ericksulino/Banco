class Cadastro:
    __slots__ = ['_lista_de_clientes']

    def __init__(self):
        self._lista_de_clientes = []

    def cadastra (self,pessoa):

        existe = self.busca(pessoa.cpf)
        if (existe == None):
            self._lista_de_clientes.append(pessoa)
            return True
        
        else:
            return False

    def busca(self,cpf):
        for lp in self._lista_de_clientes:
            if lp.cpf == cpf:
                return lp

        return None