import socket
ip = 'localhost'
port = 8001
addr = ((ip,port))
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(addr)
mensagem = ''
while(mensagem!= 'sair'):
    mensagem = input('digite uma mensagem para enviar ao servidor: ')
    client_socket.send(mensagem.encode())
    #print('mensagem enviada')
    print('mensagem recebida: '+client_socket.recv(1024).decode())

client_socket.close()