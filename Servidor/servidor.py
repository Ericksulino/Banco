from historico import Historico
from os import curdir
import socket
import sqlite3
import threading
from sqlite3.dbapi2 import Cursor
#from banco import Banco
from pessoa import Cliente
from conta import Conta

bd = sqlite3.connect('bd.sqlite')
cursor = bd.cursor()

pessoas = """CREATE TABLE IF NOT EXISTS pessoas(id integir PRIMARY KEY,nome text NOT NULL,cpf text NOT NULL,data_nascimento text NOT NULL);"""
contas = """CREATE TABLE IF NOT EXISTS contas(id integir PRIMARY KEY,numero text NOT NULL,titular text NOT NULL,saldo float NOT NULL,limite float NOT NULL);"""
historico = """CREATE TABLE IF NOT EXISTS historico(id integir PRIMARY KEY,numero_conta text NOT NULL,transacoes text NOT NULL);"""

cursor.execute(pessoas)
cursor.execute(contas)
cursor.execute(historico)

def validaConta(num,cursor):
    cnta = Conta.busca_conta(num,cursor)
    if(cnta!=False):
        return cnta
    else:
        return None

running = True

class ClienteThread(threading.Thread):

    def __init__ (self,endereco,socket,sinc):
        self.sinc = sinc
        threading.Thread.__init__(self)
        self.socket = socket

    def run(self):
        print("Conectado")

        while(True):

            recebe = self.socket.recv(1024)
            msg = recebe.decode()

            print('cliente: ' + msg)

            msg = recebe.decode().split(',')

            if recebe.decode() == 'sair':
                running = False

            elif msg[0] == 'add_cliente': # ,nome,cpf,data_nascimento
                
                if not(Cliente.cadast_clie(msg[1],msg[2],msg[3],cursor)):
                    con.send('erro'.encode())
                else:
                    con.send('sucesso'.encode())
                    bd.commit()
    
            elif msg[0] == 'add_conta': # ,numero,titular,saldo,limite
        
                if not (Conta.abrir_conta(msg[1],msg[2],msg[3],msg[3],cursor)):
                    con.send('erro'.encode())
                else:
                    con.send('sucesso'.encode())
                    bd.commit()
    
            elif msg[0] == 'transfere': # ,num,numDest,valor
        
                if not(Conta.transfere(msg[1],float(msg[2]),msg[3],cursor)):
                    con.send('erro'.encode())
                else:
                    con.send('sucesso'.encode())
                    bd.commit()
    
            elif msg[0] == 'saque': # ,num,valor
        
                if not(Conta.saca(msg[1],float(msg[2]),cursor,True)):
                    con.send('erro'.encode())
                else:
                    con.send('sucesso'.encode())
                    bd.commit()
    
            elif msg[0] == 'deposita': # ,num,valor
        
                if not(Conta.deposita(msg[1],float(msg[2]),cursor,True)):
                    con.send('erro'.encode())
                else:
                    con.send('sucesso'.encode())
                    bd.commit()

            elif msg[0] == 'saldo': # ,num
                extr = Conta.extrato(msg[1],cursor)
                if extr == None:
                    con.send('erro'.encode())
                else:
                    con.send(str(extr).encode())
                    bd.commit()

            elif msg[0] == 'busc_clie': # ,cpf
                cli = Cliente.busca_clie(msg[1],cursor)
                if cli == False:
                    con.send('erro'.encode())
                else:
                    con.send(f'{cli}'.encode())
                    bd.commit()
    
            elif msg[0] == 'busca_cnta': # ,num 
                cta = Conta.busca_conta(msg[1],cursor)
                if cta==False:
                    con.send('erro'.encode())
                else:
                    con.send(f'{cta}'.encode())
                    bd.commit()
            
            elif msg[0] == 'historic': # ,num
                hist = Historico.imprimir_transacoes(msg[1],cursor)
                if hist == None:
                    con.send('erro'.encode())
                else:
                    con.send(f'{hist}'.encode())

ip = 'localhost'
porta = 8004
endereco = ((ip,porta))
serv_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
serv_socket.bind(endereco)
sinc = threading.Lock()
print("aguardando conexão...")
serv_socket.listen(1)
con, cliente = serv_socket.accept()

print("conectado")
print("aguardando mensagem...")

while True:
    nova_thred = ClienteThread(endereco,con,sinc)
    nova_thred.start()
