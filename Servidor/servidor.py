import socket
from banco import Banco
from cliente import Cliente
from conta import Conta
class Servidor:
    def __init__(self):
        self._host = 'localhost'
        self.port = 8001
        self.addr = (self._host,self.port)
        self.serv_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.ban = Banco()
    
    def iniciar(self):
        self.serv_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.serv_socket.bind(self.addr)
        self.serv_socket.listen(10)
        print("aguardando conexão...")
        print("conectado")
        print("aguardando mensagem...")
    
    def comunicacao(self):
        con, cliente = self.serv_socket.accept()
        recebe = con.recv(1024)
        while(recebe.decode()!= 'sair'):
            print('mensagem recebida: '+ recebe.decode())
            if recebe.decode() == 'add cliente':
                nome = recebe.decode()
                cpf = recebe.decode()
                dtNas = recebe.decode()
                clie = Cliente(nome,cpf,dtNas)
                self.ban.adicionar_cliente(clie)
        
        self.serv_socket.close()
    
serv = Servidor()
serv.iniciar()