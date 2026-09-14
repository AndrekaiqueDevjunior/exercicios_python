#encapsulamento em python

#encapsulamentop significa proteger o estado interno de um objeto e controlare como os seus dados podem ser consulktados ou alterados

#no seu codigo aatual, quiialquer parte do sistem pode fazer isto

#No seu código atual, qualquer parte do sistema pode fazer isto:

ordem1.valor = -500
ordem1.status = "QUALQUER COISA"

#Isso é perigoso, porque a classe aceita valores inválidos sem nenhuma regra.

#O encapsulamento busca fazer com que alterações importantes passem por métodos controlados:

ordem1.aplicar_desconto(10)
ordem1.finalizar()
ordem1.cancelar()

#A ideia principal é:

#O objeto deve controlar a alteração do próprio estado.

# o problema do codigo sem encapsulamento é que ele permite qualquer coisa:

# no codigo atual:

self.valor = valor # aqui estamos alterando o valor do objeto ordem1
self.status = "ABERTA"

#os atributos sao publicos. Portanto, podemos fazer:

ordem1.valor = -1000
ordem1.status = "FINALIZADA E CANCELADA"

#Isso é perigoso, porque a classe aceita valores inválidos sem nenhuma regra

#ESSE CODIGO QUEBRTA AS REGRAS DA ORDEM DE SERVIÇO.

##  2. atributos publicos

## um atributo publico pode ser acessado e alterado diretamente

class OrdemServico:
    def __init__(self, valor): # metodo construtor que recebe o valor como parametro a palavra valor serve para indicar que estamos criando um atributo publico 
        self.valor = valor  # atributo publico que pode ser acessado e alterado diretamente pelo usuario 

#Uso 

ordem = OrdemServico(200)

print(ordem.valor) # chamando o atributo publico valor do objeto ordem 

ordem.valor = -500 # alterando o valor do atributo publico valor do objeto ordem

print(ordem.valor)


#EM PYTHON, UM ATRIBUTO SEM "_" OU "__" COMEÇO É CONSIDERADO UM ATRIBUTO PUBLICO E PODE SER ACESSADO 
# E ALTERADO DIRETAMENTE PELO USUARIO DENTRO DA CLASSE E FORA DA CLASSE 


self.valor
self.status
self.cliente


#3 . atributos  protegidos por convenção


#em python podemos usar um unico " _ " : 


self._valor # atributo protegido
self._status # atributo protegido 


#exemplo:

class OrdemServico:
    def __init__(self, valor):
        self._valor = valor 
        self._status = "ABERTA "

# O _ comunica :
 # este atributo é interno. Nao deveria ser alterado diretamente fora da classe.


#Porem. isso é apenas uma convenção. O python ainda permite


ordem._valor = -500 # alterando o valor do atributo protegido _valor do objeto ordem

#portando, _valor nao é realmente privado. Ele apenas avisa aaos desenvolvedor que o atributo deve ser tratado como interno.


#4.atributos privado com __ " dois under lines "

self.__valor # atributo privado
self.__status # atributo privado


#exemplo:

class OrdemServico:
    def __init__(self, valor):
        self.__valor = valor
        self.__status = "ABERTA"


#agora isto nao funciona diretamente:

ordem = OrdemServico(200) # criando um objeto da classe OrdemServico com o valor 200

print(ordem.__valor) #   

#O Python apresentará um erro semelhante a:

#AttributeError: 'OrdemServico' object has no attribute '__valor'

#Isso acontece porque o Python aplica um mecanismo chamado name mangling.
# o que é name mangling ? o python aplica um mecanismo chamado name mangling para proteger os atributos privados.    

#Internamente, o nome é transformado aproximadamente em:

_OrdemServico__valor ## aqui estamos alterando o valor do atributo privado __valor do objeto ordem 

## Importante: isso não torna o atributo completamente inacessível. 
# É uma proteção contra acesso acidental, não uma barreira de segurança absoluta.


#5. Aplicando encapsulamento à sua Ordem de Serviço

#Vamos proteger principalmente:

valor
status

#esses atributos tem regras importantes.

class OrdemServico:
    def __init__(
        self,
        numero: int,
        cliente: str,
        descricao: str,
        valor: float            
    ):
        self.numero = numero
        self.cliente = cliente
        self.descricao = descricao


        self.__valor = valor #obseve o self valor esta protegido 
        self.__status = "ABERTA" # obseve o self status esta protegido E O VALOR PADRAO É INICIADO COMO ABERTA

        #AGORAO O VALOR E O STATUS SAO INTERTNOS A CLASSE.

        # MAS SURGE UMA DUVIDA

        # COMO CONSULTAMOS ESSES DADOSA W

        # PODEMOS CRIAR METODOS DE LEITURA


