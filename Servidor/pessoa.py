class Cliente:

    def init(self, nome:str,cpf:str,data_nascimento:str):
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento

    @property
    def cpf(self):
        return self._cpf
    
    def busca_clie(buscar_cpf:str,cursor):
    
        pessoa = list(cursor.execute("SELECT * FROM pessoas WHERE cpf = {}".format(buscar_cpf)))
        if (len(pessoa)!=0):
            return pessoa[0][0]
        return False

    def cadast_clie(nome:str,cpf:str,data_nascimento:str,cursor):

        if Cliente.busca_clie(cpf,cursor)== False:
            cursor.execute("INSERT INTO pessoas(nome,cpf,data_nascimento) VALUES(?,?,?)",(nome,cpf,data_nascimento))
            return True
        return False