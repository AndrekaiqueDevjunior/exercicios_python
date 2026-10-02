#Desafio 4 — Simulador de conta bancária
#Nível intermediário
#Crie uma classe chamada ContaBancaria.
#Ela deverá possuir dois atributos:
#self.titular
#self.saldo
#Implemente três métodos:
#depositar(valor): adiciona um valor ao saldo.
#sacar(valor): retira um valor, desde que exista saldo suficiente.
#mostrar_saldo(): apresenta o nome do titular e o saldo atual.
#Crie dois objetos diferentes e faça depósitos e saques em cada um.
#Desafio extra: impeça depósitos e saques com valores negativos ou iguais a zero.


class Conta:
    def __init__(self,titular,saldo):
      self.titular = titular
      self.saldo = saldo

    def sacar(self,valor ):
       self.saldo -= valor

    def depositar(self, valor):
       self.saldo += valor

    def mostrar_saldo(self):
       print(f"Seu saldo atual é : {self.saldo} " )


conta = Conta("andré", 100) # 100

conta.sacar(50) # 50 - 100 = 50

conta.depositar(150) # 50 + 150 = 200

conta.mostrar_saldo
print(conta.saldo)