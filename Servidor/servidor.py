from os import curdir
import socket
import sqlite3
from sqlite3.dbapi2 import Cursor
#from banco import Banco
from pessoa import Cliente
from conta import Conta

host = 'localhost'
port = 8001
addr = ((host,port))
serv_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#ban = Banco()
serv_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
serv_socket.bind(addr)
serv_socket.listen(10)

print("aguardando conexão...")

con, cliente = serv_socket.accept()
print("conectado")
print("aguardando mensagem...")

bd = sqlite3.connect('bd.sqçite')
cursor = bd.cursor()

pessoas = """CREATE TABLE IF NOT EXISTS pessoas(id integir PRIMARY KEY,nome text NOT NULL,cpf text NOT NULL,data_nascimento text NOT NULL);"""
contas = """CREATE TABLE IF NOT EXISTS contas(id integir PRIMARY KEY,numero text NOT NULL,titular text NOT NULL,saldo float NOT NULL,historico text NOT NULL);"""
historico = """CREATE TABLE IF NOT EXISTS historico(id integer PRIMARY KEY,transacoes text NOT NULL);"""

cursor.execute(pessoas)
cursor.execute(contas)
cursor.execute(historico)

running = True
while(running):
    recebe = con.recv(1024)
    print('mensagem recebida: '+ recebe.decode())
    msg = recebe.decode().split(',')
    if recebe.decode() == 'sair':
        running = False

    elif msg[0] == 'add_cliente': # ,nome,cpf,data_nascimento
        
        # PAREI AQUI

        clie = Cliente(msg[1],msg[2],msg[3])
        if not(ban.adicionar_cliente(clie)):
            con.send('erro'.encode())
        else:
            con.send('sucesso'.encode())
    
    elif msg[0] == 'add_conta': # ,numero,titular,saldo,limite
        cnta = Conta(msg[1],msg[2],float(msg[3]),float(msg[4]))
        if not(ban.adcionar_conta(cnta)):
            con.send('erro'.encode())
        else:
            con.send('sucesso'.encode())
    
    elif msg[0] == 'transfere': # ,num,numDest,valor
        if not(ban.transfere(msg[1],float(msg[2]),msg[3])):
            con.send('erro'.encode())
        else:
            con.send('sucesso'.encode())
    
    elif msg[0] == 'saque': # ,num,valor
        if not(ban.saque(msg[1],float(msg[2]))):
            con.send('erro'.encode())
        else:
            con.send('sucesso'.encode())
    
    elif msg[0] == 'deposita': # ,num,valor
        if not(ban.deposita(msg[1],float(msg[2]))):
            con.send('erro'.encode())
        else:
            con.send('sucesso'.encode())

    elif msg[0] == 'saldo': # ,num
        extr = ban.extrato(msg[1])
        if extr == None:
            con.send('erro'.encode())
        else:
            con.send(str(extr).encode())

    elif msg[0] == 'busc_clie': # ,cpf
        cli = ban.busca_clie(msg[1])
        if cli == None:
            con.send('erro'.encode())
        else:
            con.send('{},{},{}'.format(cli.nome,cli.cpf,cli.data_nascimento).encode())
    
    elif msg[0] == 'busca_cnta': # ,num 
        cta = ban.busca_conta(msg[1])
        if cta==None:
            con.send('erro'.encode())
        else:
            con.send('{},{},{}'.format(cta.numero,cta.titular,cta.extrato,cta.limite).encode())
    
    elif msg[0] == 'historic': # ,num
        hist = ban.historico(msg[1])
        if hist==None:
            con.send('erro'.encode())
        else:
            con.send(hist.encode())
serv_socket.close()


