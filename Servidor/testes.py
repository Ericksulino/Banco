from conta import Conta
from pessoa import Cliente
from banco import Banco
def true_false(bol):
    if bol == True:
        print("Sucesso!")
    else: print("Não foi possível!")

ban = Banco()

cl1 = Cliente('Erick',123,16/12/2000)
ban.adicionar_cliente(cl1)
cl2 = Cliente('Jose',321,12/10/1997)
ban.adicionar_cliente(cl2)

c1 = Conta(123,cl1,100,1000)
ban.adcionar_conta(c1)
c2 = Conta(432,cl2,850,1000)
ban.adcionar_conta(c2)

print(ban.busca_conta(432))

print("Depositos:")
true_false(c1.deposita(10))
true_false(c1.deposita(900))

print("\n\nSaques:")
true_false(c1.saca(20))
true_false(c1.saca(100))

print("\n\nTransferencias:")
true_false(ban.transfere(c1.numero,c2.numero,50))
true_false(c2.transfere(1000,c1))

print("\n\nExtratos")
print(ban.extrato(123))
print(c2.extrato())

print("\n\nHistorico")
print(c1.ver_historico())
print(c2.ver_historico())

print(Conta.get_total_contas())