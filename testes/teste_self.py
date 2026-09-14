class Conta:

    def __init__(self, saldo):
        self.saldo = saldo


    def creditar(self, valor):
        self.saldo += valor


conta = Conta(100)  # conta é o bjeto , Conta é a classe


print(conta.saldo) 

conta.creditar(50)

print(conta.saldo)
