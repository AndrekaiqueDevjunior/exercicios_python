### 16. Herança de métodos




#classe pai: 

class Funcionario:

    #vou criar uma funcao que recebe self como parametro :  e printa funcionario trabalhando # bem basico

    def trabalhar(self)
        print("Funcionario trabalhando")

###classe filha:


class Desenvolvedor(Funcionario): # a classe Desenvolvedor é uma classe filha que herda atributos e metodos da classe PAI FUNCIONARIO.

    def programar(self):
        print("usando o chat gpt na cara dura eo claude code")

###então:

##vou criar um objeto que instancia da Classe filha Desenvolvedor

dev = Desenvolvedor() # ela é um objeto que instancia da Classe filha Desenvolvedor 
##porque dev consegue usar o metodo programar ? porque a classe Desenvolvedor herda o metodo programar da classe Pai Funcionario
#


###pode usar:

dev.trabalhar() # estamos usando o metodo trabalhar da classe pai Funcionario
dev.programar() # estamos usando o metodo programar da classe filha Desenvolvedor

## por que estamos conseguindo usar o metodo trabalhar ? porque a classe Desenvolvedor herda o metodo trabalhar da classe Pai Funcionario

## e também deixando como parametro da classe Desenvolvedor( o parametro Funcionario) o objeto dev que eh uma instancia da classe Desenvolvedor

#sobrescrita de metodo (trabalhar): 


## podemos alterar um método herdado

#agora chegamos perto de polimorfismo.

#classe pai:

class Funcionario:

    def trabalhar(self): #metodo trabalhar
        print("Realizando trabalho")

#Filho:

class Desenvolvedor(Funcionario): # a classe Desenvolvedor eh uma classe filha que herda atributos e metodos da classe PAI FUNCIONARIO.

    def trabalhar(self): #metodo trabalhar
        print("Programando")

#Agora:

dev = Desenvolvedor()

dev.trabalhar()

##resultado:

Programando

#apenas de existir:


Funcionario.trabalhar()

#A classe filha criouy sua propria versao.

#isso é chamado de:

##sobrescrita de metodo

#em inglês:

##method override (SOBRESCRITAS DE METODO )


## 17. PODEMOS ALTERAR UM METODO HERDADO 

###AGORA CHEGAMOS PERTO DE POLIMORFISMO

#CLASSE PAI: 

class Funcionario: #cLASSE PAI

    def trabalhar(self): #metodo trabalhar
        print("Realizando trabalho") # metodo trabalhar da classe pai Funcionario 

#Filho:

class Desenvolvedor(Funcionario): # a classe Desenvolvedor eh uma classe filha que herda atributos e metodos da classe PAI FUNCIONARIO.

    def trabalhar(self): #metodo trabalhar
        print("Programando") # metodo trabalhar da classe filha Desenvolvedor 

#Agora:

dev = Desenvolvedor()

dev.trabalhar()

##resultado:    

Programando

#APESAR DE EXISTIR: 

funcionario.trabalhar()

#a classe filha criou sua propria versao.

### isso é chamado de:

##sobrescrita de metodo


##18. override nao significa criar outro metodo

## observe:

#classe pai:

def trabalhar(self) # funcao trabalhar com parametro self


#classe filha:

def trabalhar(self) # funcao trabalhar com parametro self

#mesmo nome.

#a filha esta dizendo:

## para mim, esse comportamento funciona de outra maneira".

##isso é muito importante em POO.


##19. podemos usar super() em métodos normais tambem

##super nao serve apenas para:

## herdar atributos e metodos ou pegar o metodo construtor da Classe pai.


#exemplo:

class Funcionario:


    def trabalhar(self):
        print("Iniciando trabalho")



##filho:

class Desenvolvedor(Funcionario):

    def trabalhar(self)

        super().trabalhar()

        print("Programando API EM FLASK")


        ##executando

dev = Desenvolvedor() ## estamos criando um objeto chamado  dev para instancia da classe Desenvolvedor 
# com isso conseguimos usar o metodo trabalhar da classe pai Funcionario

dev.trabalhar() ## estamos usando o metodo trabalhar da classe pai Funcionario
## quer dizer : iniciando trabalho programando api em flask 

## relembrando o que dev.trabalhar faz : 
##estamos acessando o metodo trabalhar da classe pai Funcionario e estamos executando o metodo trabalhar da classe pai Funcionario

## como a agente acessa? usamos um (.) para acessar o metodo trabalhar da classe pai Funcionario

## entao se eu quiser acessar o metodo trabalhar da classe filha Desenvolvedor eu preciso: colocar um ponto (.) antes do metodo trabalhar da classe filha Desenvolvedor


##20. um exemplo completo

class Usuario:

    def __init__(self, nome, email): # estamos criando um metodo construtor da classe Usuario, que recebe 
        #parametros nome e email 
        self.nome = nome # aqui estamos criando um atributo nome que recebe o valor do parametro nome
        self.email = email # aqui estamos criando um atributo email que recebe o valor do parametro email que pode ser uma instancia da classe Usuario
        ##ou ser usado por um objeto da classe Usuario

    #funcao exibir_dados com parametro self  que é uma instancia da classe Usuario, instancia que é um constructor da classe Usuario
    def exibir_dados(self):
        print(self.nome) # aqui estamos usando o atributo {self.nome} da instancia da classe Usuario
        print(self.email) # aqui estamos usando o atributo {self.email} da instancia da classe Usuario


class Administrador(Usuario):

    def __init__(self, nome, email, nivel):

        super().__init__(nome, email)

        self.nivel = nivel # aqui estamos criando um atributo nivel que recebe o valor do parametro nivel
        # esse atributo {self.nivel} é unico do administrador, porem ele ainda herda os dados de nome e email da instancia da classe Usuario


    def exibir_dados(self):

        super().exibir_dados() # estamos herdando o metodo exibir_dados da classe pai Usuario

        print(self.nivel) # aqui estamos usando o atributo {self.nivel} da instancia da classe Administrador

### criando:

#objeto admin que recebe  classe administrador e instancia da classe Administrador


admin = Administrador(
    "André",

    "andre@email.com",
    "SUPER_ADMIN"    
    _)


#resultado: 
André
andre@email.com
SUPER_ADMIN

 ##24.python tambem permite herança multipla


 #exemplo:

class Voador: # classe Voador
    pass # pass significa nao fazer nada

class Nadador: # classe Nadador 
    pass # pass significa nao fazer nada

class Pato(Voador, Nadador): # 
    pass


#pato herda de duas classes.

# mas nao recomendo aprofundarmos nisso agora

## herança multipla envolve um conceito chamado:

#MRO (Method Resolution Order)

# metodo resolução ordem  = MRO ( Method Resolution Order)


#25 . erros comuns

#erro 1 - esquecer o super()


class Pessoa:

    def __init__(self, nome): #criando o metodo construtor com self que recebe o parametro nome
        self.nome = nome # aqui estamos criando um atributo nome que recebe o valor do parametro nome
        #self serve para indicar que estamos criando um metodo de instancia
        # o que eh metodo de instancia  = um metodo que pertence a classe e representa um comportamento do objeto
        # que pode ser : trabalhar, comer, dormir, etc.


class Funcionario(Pessoa):


    def __init__(self, nome, salario):
        self.salario = salario

#aqui o cenario estamos criando uma classe Funcionario que herda atributos da Classe pai pessoa
# logo em seguida estamos criando um metodo construtor com parabentros serve quew serve parai ndiciar que estamos criando um metodo de instancia.
## em seguida no parametro do metodo construtor, temos nome  e salario.
## logo depois estamos self. salario que recebe salario = salario que eh um parametro do metodo construtor

## significado de self.salario = salario 
### significa:
### pegue o valor recebido no parametro salario e salve dentro do objeto no atributo self.salario


## mentalmente: 

## self.nome = nome
## atributo  Parametro


class Usuario: ## acabei de aprender se uma classe é Pai, ela nao precisa () pois nao irá ter parametros na classe, mas no construtor. 


    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


class Aluno(Usuario):

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


### guardar esta formula:

self.alguma coisa = alguma coisa
       ↑                 ↑
atributo do objeto  valor recebido

### Objeto() -> cria uma instancia
### obj  -> GUARDA UAM REFERENCIA PARA ESSA INSTÂNCIA


###PENSE ASSIM:

Class Pessoa:

    pass

#Pessoa é a classe. Ela funciona como um ModuleNotFoundError

#quando fazxemos:

## obj = Pessoa()

##obj  -> GUARDA UAM REFERENCIA PARA ESSA INSTÂNCIA

## o techo:

#cria um objeto, tamberm chamado de instancia da classe Pessoa.mro

#E:
#obj

##  obj = Pessoa() <---- cria um objeto da classe Pessoa

##pode ser lido como:
## crie um objeto da classe Pessoa e faça a variavel obj apontar para ele
## o objeto se chama = obj