class cliente:
    def __init__(self, nome, idade): ## __init__ eh um metodo especial que eh chamado automaticamente quando criamos um objeto da classe
        ## init quer dizer : construtor da classe cliente 
        self.nome = nome ## self quer dizer: essa classe que estou criando tem esse atributo nome e esse atributo idade tem esse valor 
        ## self é igual this em outras linguagens , self quer dizer: essa classe que estou criando tem esse atributo nome e esse atributo idade tem esse valor 
        ## self quer dizer: essa classe que estou criando tem esse atributo nome e esse atributo idade tem esse valor
        self.idade = idade  


#correspondencia    

#typescript e python
# class             |   class
# constructor       |   __init__ 
# this              |   self
# new cliente()     |   Cliente()

#criando um objeto

#Typescript

#const cliente = new Cliente("André");

#Python

cliente = Cliente("André");


#em python naop usamos new;

#ao executar

#cliente = Cliente("André");

# o python:


#  1 cria um objeto da classe cliente;
# 2 chama automaticamente o metodo __init__  que é um construtor da classe cliente;
# 3 passa o objeto criadoi pelo parametreo self para o construtor; 
# 4 passa "andré" para o parmetro nome;

#o que significa self ?


#no typescript usamos:

# this.nome

# no python usamos:

# self.nome

#self significa : 

    # este objeto atual


#exemplo: 

class cliente:
    def __init__ (self, nome: str): # __init__ eh um metodo especial que eh chamado automaticamente quando criamos um objeto da classe
        # init quer dizer : construtor da classe cliente

        self.nome = nome # self quer dizer: essa classe que estou criando tem esse atributo nome e esse atributo idade tem esse valor

# nesta linha

self.nome = nome

#temos duas coisas diferentes:

self.nome

#é o atributo armazenado o nome do cliente;

nome

#é o parmetro da funcao __init__


# o atributo nomne deste objeto recebera o nome passado na criacao do objeto .



#classe ordem de servico em python


class OrdemServico:
    def __init__( # __init__ é um metodo especial que é chamado automaticamente quando criamos um objeto da classe
        # init é um construtor da classe OrdemServico que recebe os parametros descricao, cliente e valor como parametros 

        self, 
        cliente: str, # STR VEM DE STRING EM PYTHON QUE SIGNIFICA QUE ACEITA  ABC EM PYTHON  TIPO " SORRISO RONALDO "
        descricao: str,  # STR DESCRICAO DA ORDEM DE SERVICO 
        valor: float # FLOAT VEM DE FLOAT EM PYTHON QUE SIGNIFICA QUE ACEITA NUMEROS DECIMAIS TIPO 3.14 

            
    ): 
        self.cliente = cliente ## self quer dizer: essa classe que estou criando tem esse atributo nome e esse atributo idade tem esse valor
        self.descricao = descricao
        self.valor = valor
        self.status = "ABERTA"

        #criando uma OS:

        ordem = ordemServico( # estamos instanciando a classe ordemServico com os parametros descricao, cliente e valor
            # por que estamos fazendo isso ? porque estamos criando um objeto da classe ordemServico  
            cliente="andré",
            descricao="Manutencao do computador",
            valor=250.00 

        )

        #acessando atributos:


        print(ordem.cliente) # por que  ordem.cliente ? porque estamos acessando o atributo cliente da classe ordemServico
        print(ordem.descricao) # por que  ordem.descricao ? porque estamos acessando o atributo descricao da classe ordemServico
        print(ordem.valor) # por que  ordem.valor ? porque estamos acessando o atributo valor da classe ordemServico
        print(ordem.status) # por que  ordem.status ? porque estamos acessando o atributo status da classe ordemServico
        #por que precisamos acessar esses atributos ? porque estamos querendo imprimir os valores desses atributos na tela

        # resultado


        #andré
        #manutencao de computador
        #250.0
        #ABERTA


        #metodo em python

        #no typescrip´t:

        # finalizar(): void {
            #this.status = "FINALIZADA";
        
        #}

        #revisao classe o objeto





#fundamento do POO :
#classe e objeto
#metodo construtor __init__
## significado do self;
## atributos de instancia
## criacao de objetos

## introducao aos metodos

## o proximo passo é consolidar metodos de instancia e depois avançar para encapsulamento.

##reviisao: classe e objeto


        class OrdemServico:
            def _init_(self, numero, cliente,descricao);
                self.numero = numero
                self.cliente = cliente
                self.descricao = descricao
                self.status = "ABERTA"


                #aqui a OrdemServico é a classe, ou seja, o molde


                #aqui estamos criando um objeto da classe OrdemServico com os parametros numero, cliente e descricao


                ordem1 = OrdemServico(
                    1,
                    "André",
                    "Manutencao de computador"



                )
                #aqui,ordem1 é um objeto, ou seja, uma instancia da classe OrdemServico.


## 2 . o que é um metodo de instancia.

## um metodo é uma funcao que pertence a classe e representa um comportamento do objeto

class OrdemServico:
    def __init__(self, numero, cliente,descricao): # AQUI ESTAMOS: CRIANDO UM METODO DE INSTANCIA 
        # que recebe os parametros numero, cliente e descricao, self serve para indicar que estamos criando um metodo de instancia
        # o que é um metodo de instancia = um metodo que pertence a classe e representa um comportamento do objeto
        self.numero = numero
        self.cliente = cliente
        self.descricao = descricao
        self.status = "ABERTA"

        def finalizar(self):
            self.status = "FINALIZADA"

            #o metodo

            def finalizar(self): # esse é o metodo

    # é chamado de metodo de instancia, porque atua sobre uma instancia específica da classe.

#utilizacao 

ordem1 = OrdemServico(
    1,
    "André",
    "Manutencao de computador"
)

print(ordem1.status)

ordem1.finalizar() # aqui estamos chamando o metodo finalizar

print(ordem1.status)    


#resultado:

ABERTA
FINALIZADA


#quando fazemos:

ordem1.finalizar()

#o python envia ordem1 automaticamente para o parametro self.


# conceitualmente, é parecido com 

OrdemServico.finalizar(ordem1)  



#porque usamos self ?

# o self represenmta o objeto atual.

self.status = "FINALIZADA"



#SIGNIFICA:
#altere o atributo status deste objeto especifico para "FINALIZADA".

#por isso cada ordem,, mantem seu proprio estado:


ordem1 = OrdemServico(1, "André", "Manutencao de computador") # aqui estamos criando um objeto da classe OrdemServico com os parametros 
#numero, cliente e descricao


ordem2 = OrdemServico(2, "Kaique", "Formatação de computador")# aqui estamos criando um objeto da classe OrdemServico com os parametros
# numero, cliente e descricao



ordem1.finalizar() #estamos finalizando a ordem 1 e nao a ordem 2
ordem2.finalizar() # estamos finalizando a ordem 2 e nao a ordem 1 

print(ordem1.status)
print(ordem2.status)        


#4. Metodo que recebe parametros.

# podemos criar um metodo qpara adicionar um servico e seu valor:


class OrdemServico:
    def __init__(self, numero, cliente,descricao): # AQUI ESTAMOS: CRIANDO UM METODO DE INSTANCIA 
        # que recebe os parametros numero, cliente e descricao, self serve para indicar que estamos criando um metodo de instancia
        # o que é um metodo de instancia = um metodo que pertence a classe e representa um comportamento do objeto
        self.numero = numero
        self.cliente = cliente
        self.descricao = descricao
        self.status = "ABERTA"
        self.valor = 0.0

        def definir_valor(self, novo_valor):
            self.valor = novo_valor 

# uso:


ordem1 = OrdemServico(
    1,
    "André",
    "Manutencao de computador"
)


ordem1.definir_valor(150.00)

print(ordem1.valor) 


#nesse metodo:

def definir_valor(self, novo_valor):

    #temos dois parametros: 
    #self: objeto que esta executando o método;
    #novo_valor: valor enviado durante a chamada.

    #na chamada:


    ordem1.definir_valor(150.00)

    #150.00 é o argumento atribuido ao parametro novo_valor

#5. metodo que retorna um valor

#um metodo tamem pode calcular e devolver informacoes:


class OrdemServico:
    def __init__(self, numero, cliente, valor): # AQUI ESTAMOS: CRIANDO UM METODO DE INSTANCIA 
    self.numero = numero
    self.cliente = cliente
    self.valor = valor
 
    def calcular_valor_com_desconto(self, percentual): # aqui estamos criando um metodo de instancia que recebe um parametro percentual que representa o desconto
        # que queremos aplicar ao valor da ordem de servico self serve para indicar que estamos criando um metodo de instancia 
        #percental é um parametro do metodo calcular_valor_com_desconto
        desconto = self.valor * percentual / 100
        valor_final = self.valor - desconto

        return valor_final


#uso:

ordem1 = OrdemServico(1, 
    "André", 
    200.00
    )

resultado = ordem1.calcular_valor_com_desconto(10)



print(resultado)

#resultado:
# 180.0

#observe

self.valor

# é um atributo do objeto.

# percentual

# é um parametro do método


desconto
valor_final


#6 nosso primeiro modelo completo

class OrdemServico:
    def __init__(
        self,
        numero: int, # numeros inteiros 
        cliente: str, # strings = texto em python 
        descricao: str, # strings = texto em python 
        valor: float # numeros decimais exemplo: 3.14
    ):
        self.numero = numero
        self.cliente = cliente
        self.descricao = descricao
        self.valor = valor 
        self.status = "ABERTA"

    def finalizar(self) -> None: # none é igual a void em java # -> None significa que o metodo nao retorna nenhum valor
        self.status = "FINALIZADA"

    def cancelar(self) -> None: # none eh igual a void em java # -> None significa que o metodo nao retorna nenhum valor
        self.status = "CANCELADA"

    def aplicar_desconto(self, percentual: float) -> None: # -> None significa que o metodo nao retorna nenhum valor
        desconto = self.valor * percentual / 100 # desconto = self.valor * percentual / 100 
        self.valor -= desconto # self.valor = self.valor - desconto 


    def exibir_resumo(self) -> str: # -> str significa que o metodo retorna uma string
        return (
            f"OS #{self.numero}| " #f é uma string formatada # | e uma barra vertical F significa = formatar 
            f"Cliente: {self.cliente} |  "
            f"Status: {self.status}" | #  
            f"Valor: R$ {self.valor:.2f}" # :.2f significa que o valor vai ter 2 casas decimais exenplo 3.14 vai ser 3.14
            
        )