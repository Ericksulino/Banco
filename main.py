from conta import Conta
from cliente import Cliente

def true_false(bol):
    if bol == True:
        print("Sucesso!")
    else: print("Não foi possível!")

cl1 = Cliente('Erick',123,16/12/2000)
cl2 = Cliente('Jose',321,12/10/1997)

c1 = Conta(123,cl1,100,1000)
c2 = Conta(432,cl2,850,1000)



print("Depositos:")
true_false(c1.deposita(10))
true_false(c1.deposita(900))

print("\n\nSaques:")
true_false(c1.saca(20))
true_false(c1.saca(100))

print("\n\nTransferencias:")
true_false(c1.transfere(50,c2))
true_false(c2.transfere(1000,c1))

print("\n\nExtratos")
c1.extrato()
c2.extrato()

print("\n\nHistorico")
c1.ver_historico()
c2.ver_historico()

print(Conta.get_total_contas())

