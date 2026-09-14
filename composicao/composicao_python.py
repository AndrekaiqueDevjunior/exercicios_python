#### COMPOSIÇÃO ####



class Motor: ### é uma classe que necessariamente precisa ter herança

    def ligar(self):
        print("Motor Ligado")


###agora:

class Carro: 

    def  __init__(self): ### aqui estamos criando o metodo construtor da classe carro 
        self.motor = Motor() ### aqui estamos criando um objeto motor que pertence ao carro


##aqui:

self.motor = Motor() ## aqui estamos criando um objeto motor que pertence ao carro

## estamos fazendo uma composição aonde o carro tem um motor que pertence ao carro então usamos o termo:
## TEM UM OBJETO MOTOR QUE PERTENCE AO CARRO

## significa :
## o objeto Carro possui um objeto Motor.

#na classe carro que estamos tratando
## composição entre Carro e Motor

## tem uma observação que deixamos passar,
## passamos o método construtor usando
## ()

## exemplo self.motor = Motor()

## enquanto um metodo constructor padrao, passa 
## self.motor = Motor() dentro da classe Carro

## desclaimer pq nao faz sentido herança de carro e motor
#
# Carro É UM Motor
## NAO, carro é um carro, motor é um objeto que faz parte de um motor7


## composicao recebendo o objeto
## o que é composicao significa que uma classe usa outras classes.
## uma classe usa outras classes. 

#existe uma forma ainda melhor:

class Motor: #@ classe motor

    def ligar(self): # metodo ligar
        print("Motor Ligado")


class Carro:

    def __init__(self, motor):
        self.motor = motor


## criamos um objeto motor que recebe a classe motor

motor = Motor()
##depois:

carro = Carro(motor) ## criamos um objeto carro que recebe o objeto motor
## entao estamos criando um objeto carro que recebe um objeto motor e Carro recebe um objeto motor como parametro que eh uma instancia da classe motor

motor = Motor()

#criamos um objeto motor


carro = Carro(motor)



##entregamos o motor para o carro e o carro recebe o motor 

## dentro do carro:

#self.motor = motor 


##voltamos exatamente aquela ideia que voce perguntou antes:

#self.motor = motor
#    ↑         ↑
#atributo     objeto recebido

##composicao com ordem de serviço
##agora um exemplo mais util para backend  


## imagina

class Cliente: # classe cliente

    def __init__(self, nome, email): # metodo construtor 
        self.nome = nome # atributo  
        self.email = email# atributo

#agora uma ordem de servico# 
class OrdemServico:

    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente


#criamos o cliente:

cliente = Cliente( #criamos um objeto da classe cliente , o nome do objeto é "cliente", com C minuscula, 
    #o primeiro argumento eh o nome do cliente e o segundo eh o email do cliente
    "André", # o primeiro argumento eh o nome do cliente e o segundo eh o email do cliente
    "andre@email.com" # o primeiro argumento eh o nome do cliente e o segundo eh o email do cliente
)

##depois:

ordem = OrdemServico(
    100, # numero 
    cliente # objeto da classe cliente
)

#Agora temos:

#OrdemServico
   # │
    #└── TEM UM Cliente

##podemoss acessar:

print(ordem.numero) # acessando o atributo numero do objeto ordem, esse numero veio da classe OrdemServico
print(ordem.cliente.nome) # acessando o atributo nome do objeto cliente , esse nome veio da classe Cliente
print(ordem.cliente.email) # acessando o atributo email do objeto cliente , esse email veio da classe Cliente 


## perceba isto:

ordem.cliente.nome 

## podemos quebrar em etapas:

ordem

##acesseo objeto OrdemServico.

##depois:

ordem.cliente

##acesse o objeto Cliente que está dentro da ordem.

##depois:

ordem.cliente.nome

## acesse o atributo nome desse cliente


##mentalmente:



#ordem ##acesseo objeto OrdemServico.
# ↓
#[ OrdemServico ] ##acesseo objeto OrdemServico.

   #    │
  #     ├── numero = 100
  #     │
   #    └── cliente ─────→ [ Cliente ] ##acesse o objeto Cliente que está dentro da ordem.
     #                         │
   #                           ├── nome = André ## acesse o atributo nome desse cliente
    #                          └── email = ...


##explicando por que nao usamos herança e sim composicao


## seria estranho dizer, Ordem de Servico '' É UM " Cliente.
# 
# nao é verdade
# 
# o correto é dizer 
# ordem de servico >>>>>>>>>>>>>>>>>>>>>>TEM UM Cliente <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 
# 
#por isso:"

class OrdemServico: # criamos a classe OrdemServico

    def __init__(self, cliente): # criamos um metodo construtor 
        self.cliente = cliente # criamos um atributo que recebe um objeto da classe cliente