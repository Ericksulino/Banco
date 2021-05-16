import socket
class Servidor:
    def __init__(self):
        self._host = 'localhost'
        self.port = 8001
        self.addr = (self._host,self.port)
        self.serv_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    def iniciar(self):
        self.serv_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.serv_socket.bind(self.addr)
        self.serv_socket.listen(10)
        print("aguardando conexão...")
        print("conectado")
        print("aguardando mensagem...")
        con, cliente = self.serv_socket.accept()
        enviar = input('digite uma mensagem para enviar ao cliente: ')
        con.send(enviar.encode())
        enviar = ''
        while(enviar!= 'sair'):
            recebe = con.recv(1024)
            print('mensagem recebida: '+ recebe.decode())
            enviar = input('digite uma mensagem para enviar ao cliente: ')
            con.send(enviar.encode())
        
        self.serv_socket.close()

serv = Servidor()
serv.iniciar()