class Cliente ():
    

    __slots__ = ['_nome','_cpf','_data_nascimento']
    def __init__(self, nome, cpf, data_nascimento):
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,nm):
        self._nome = nm

    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self,cp):
        self._cpf = cp

    @property
    def data_nascimento(self):
        return self._data_nascimento
    
    @data_nascimento.setter
    def data_nascimento(self,dt):
        self._data_nascimento = dt

    def imprimir_pessoa(self):
        print(self._nome, ", CPF: ", self._cpf,"Data de nascimento: ",self._data_nascimento)