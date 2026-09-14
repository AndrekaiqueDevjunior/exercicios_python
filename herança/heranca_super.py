##10. Entrando o super()
##A solução:


class Pessoa:

    def __init__(self, nome , email):
        self.nome = nome
        self.email = email


class Tecnico(Pessoa):          ## Tecnico eh uma especializacao de Pessoa

    def __init__(self, nome, email, especialidade): ## no caso esse metodo eh o construtor da classe Tecnico 


        super().__init__(nome , email) ## o super eh chamado automaticamente quando criamos um objeto da classe Tecnico.

        ##usamos o super para chamar o construtor da classe Pessoa

        self.especialidade = especialidade ## no caso esse metodo eh o construtor da classe Tecnico 


## agora:

tecnico = Tecnico( # instanciando a classe Tecnico com os parametros passados como parametros do constructor da classe Tecnico
    "André",
    "andremail.com",
    "Backend"
)


##podemos acessar:

print(tecnico.nome)
print(tecnico.email)
print(tecnico.especialidade)



#resultado:

André # isso é uma saida de uma instancia da classe Tecnico dos parametros passados como parametros do constructor da classe Tecnico
andremail.com
Backend



## 11 . o que significa super()?

#essa linha:

super().__init__(nome, email) # o super eh chamado automaticamente quando criamos um objeto da classe Tecnico. ele eh o construtor da classe Pessoa.


###No nosso exemplo:

#Tecnico
  # ↓
#super()
  # ↓
#Pessoa
   #↓
#Pessoa.__init__()


## 12.fluxo completo

## quando fazemos:

# estamos instanciando
tecnico = Tecnico(
    "Ana Maria "
    "pitukinhBemFofinha@gmail.com"
    "Audio Visual Assistant"
)

#o python entra aqui:

def __init__(self, nome, email, especialidade): 

##depois encontra:

super().__init__(nome, email) # o super eh chamado automaticamente quando criamos um objeto da classe Tecnico. ele eh o construtor da classe Pessoa.]
#mas vale ressaltar que super chama um construtor da classe Pessoa que é uma classe PAI.
# ele chama o construtor da classe pai que no caso é a classe chamada Pessoa

#entao vai para:

Pessoa.__init__() 

#executa:

self.nome = nome
self.email = email 

#volta para tecnico. 

#depois executa:

self.especialidade = especialidade

#resultado final:

nome = "Ana Maria "
email = "pitukinhBemFofinha@gmail.com"
especialidade = "Audio Visual Assistant"



#13. exemplo no sistema de Ordem de Serviço

#vamos trazer para algo mais proximo de backend.

#podemos ter uma classe genérica:

class Documento:

    def __init__(self,
                 numero,
                 cliente):
        self.numero = numero # no caso esse metodo eh o construtor da classe Documento 
        self.cliente = cliente# no caso esse metodo eh o construtor da classe Documento. Self quer dizer: essa classe que estou 
        #criando tem esse atributo nome e esse atributo idade tem esse valor


    #funcao que vai exibir um numero (parametro self)

    def exibir_numero(self):
        return self.numero

#agora uma ordem de serviço

## vamos criar uma classe OrdemServico( que recebe como parametro a classe pai Documento)


class OrdemServico(Documento):

    #metodo construtor da classe OrdemServico  . 
    def __init__ (self, numero, cliente, descricao):

        super().__init__(numero, cliente) # o super eh chamado automaticamente quando criamos um objeto da classe OrdemServico. 
        #ele eh o construtor da classe Documento.
        # de forma mais didatica, estamos chamando um metodo construtor de uma classe Pai que eh a classe Documento que eh a classe pai de OrdemServico 

        self.fornecedor = fornecedor # no caso esse metodo eh o construtor da classe OrdemServico 
    
        ##por que usamo super ? porque o super eh um metodo especial que eh chamado automaticamente quando criamos um objeto da classe.
        # ele eh o construtor da classe OrdemServico


class OrdemCompra(Documento):

    def __init__(self, numero, cliente, fornecedor):


        #estamos chamando a classe DOcumento usando o metodo especial .

        super().__init__(numero,cliente) # o super eh chamado automaticamente quando criamos um objeto da classe OrdemCompra. 
        #ele eh o construtor Pai  da classe Documento que também é uma classe Pai
        # de forma mais didatica, estamos chamando um metodo construtor de uma classe Pai que eh a classe Documento que eh a classe pai de OrdemCompra 


        self.fornecedor = fornecedor


## temos esse seguinte desenho de herança:

                  Documento # Classe Pai
                 /         \
                /           \
      OrdemServico       OrdemCompra # classe filha de Documento
# classe Filha (OrdemServico) herda os atributos e metodos da classe Pai (Documento)

#ambas possuem:
numero
cliente
exibir_numero()

#mas cada uma possui suas proprias características e comportamentos. 
#exemplo: a classe OrdemServico possui um atributo fornecedor e a classe OrdemCompra possui um atributo fornecedor

#ou seja: Ordem servico com atributo fornecedor e OrdemCompra com atributo fornecedor


## 14. usando 

#vamos criar um objeto chamado os que recebe OrdemServico ( classe filha de Documento)

os = OrdemServico(
     100,
     "Empresa XPTO",
     "Manutenção de servidor"
)

#entao conseguimos acessar ele da seguinte forma.

print(os.numero)
print(os.cliente)
print(os.descricao)


## e podemos usar o metodo herdado:

print(os.exibir_numero())   

#mesmo que exibir_numero() nao estando dentro de:

OrdemServico

#ele veio de:

Documento # classe Pai, entao tem que respeitar o fluxo de herança 



#hora de refletir:

## 15. a ideia de "É UM"

#EXISTE UMA REGRa mental muito boa para saber se herança faz sentido

#pergunte:

# a classe filha é um tipo da classe pai ?

#por exemplo:

#Cachorro é um tipo de animal

#faz sentido.

#gerente é um funcionário


#faz sentido

#ordemServico é UM documento ?


#faz sentido
#mas:

#Carro é UM motor

#nao
#um carro:

    #tem um motor.

#esse caso normalmente seria (composicao) e nao herança
#relembrando de composicao a composicao significa que uma classe usa outras classes. 
# uma classe usa outras classes.