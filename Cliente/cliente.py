import socket
class Cliente:
    def __init__(self):
        self._ip = 'localhost'
        self._port = 8001
        self._addr = ((self._ip,self._port))
        self._client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def cli_sock_set(self,css):
        self._client_socket = css

    def comunicacao(self):
        self._client_socket.connect(self._addr)
        mensagem = ''
        while(mensagem!= 'sair'):
            mensagem = input('digite uma mensagem para enviar ao servidor: ')
            self._client_socket.send(mensagem.encode())
            #print('mensagem enviada')
            print('mensagem recebida: '+self._client_socket.recv(1024).decode())

        self._client_socket.close()

clie = Cliente()
clie.comunicacao()