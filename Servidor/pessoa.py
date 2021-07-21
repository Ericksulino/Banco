class Cliente:

    def init(self, nome:str,cpf:str,data_nascimento:str):
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento

    @property
    def cpf(self):
        return self._cpf
    
    def busca_clie(buscar_cpf:str,cursor):
    
        cursor.execute('SELECT cpf,nome,data_nascimento FROM pessoas')
        
        for pessoa in cursor:
            if (pessoa[0] == buscar_cpf):
                return pessoa
        return False

    def cadast_clie(nome:str,cpf:str,data_nascimento:str,cursor):

        if (Cliente.busca_clie(cpf,cursor)) == False:
            cursor.execute("INSERT INTO pessoas(nome,cpf,data_nascimento) VALUES(%s,%s,%s)",(nome,cpf,data_nascimento))
            return True
        return False