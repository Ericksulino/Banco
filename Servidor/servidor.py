import socket
from banco import Banco
from pessoa import Cliente
from conta import Conta

host = 'localhost'
port = 8001
addr = ((host,port))
serv_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ban = Banco()
serv_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
serv_socket.bind(addr)
serv_socket.listen(10)

print("aguardando conexão...")
con, cliente = serv_socket.accept()
print("conectado")
print("aguardando mensagem...")
running = True
while(running):
    recebe = con.recv(1024)
    print('mensagem recebida: '+ recebe.decode())
    if recebe.decode() == 'sair':
        running = False
    elif recebe.decode() == 'add cliente':
        con.send('nome:'.encode())
        nome = recebe.decode()
        con.send('cpf:'.encode())
        cpf = recebe.decode()
        con.send('dtNas:'.encode())
        dtNas = recebe.decode()
        clie = Cliente(nome,cpf,dtNas)
        if not(ban.adicionar_cliente(clie)):
            con.send('erro'.encode())
            
serv_socket.close()
