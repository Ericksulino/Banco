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
    msg = recebe.decode().split(',')
    if recebe.decode() == 'sair':
        running = False

    elif msg[0] == 'add_cliente':
        clie = Cliente(msg[1],msg[2],msg[3])
        if not(ban.adicionar_cliente(clie)):
            con.send('erro'.encode())
        else:
            con.send('sucesso'.encode())
    
    elif msg[0] == 'add_conta':
        cnta = Conta(msg[1],msg[2],float(msg[3]),float(msg[4]))
        if not(ban.adcionar_conta(cnta)):
            con.send('erro'.encode())
        else:
            con.send('sucesso'.encode())
    
    elif msg[0] == 'transfere':
        if not(ban.transfere(msg[1],msg[2],float(msg[3]))):
            con.send('erro'.encode())
        else:
            con.send('sucesso'.encode())
    
    elif msg[0] == 'saque':
        if not(ban.saque(msg[1],float(msg[2]))):
            con.send('erro'.encode())
        else:
            con.send('sucesso'.encode())
    
    elif msg[0] == 'deposita':
        if not(ban.deposita(msg[1],float(msg[2]))):
            con.send('erro'.encode())
        else:
            con.send('sucesso'.encode())

    elif msg[0] == 'saldo':
        if not(ban.extrato(msg[1])):
            con.send('erro'.encode())
        else:
            con.send('sucesso'.encode())

    elif msg[0] == 'busc_clie':
        if not(ban.busca_clie(msg[1])):
            con.send('erro'.encode())
        else:
            con.send('sucesso'.encode())
    
    elif msg[0] == 'busca_cnta':
        if not(ban.busca_conta(msg[1])):
            con.send('erro'.encode())
        else:
            con.send('sucesso'.encode())
serv_socket.close()


