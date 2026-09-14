class OrdemServico:
    empresa = "Andryll Solutions"

    def __init__(self, numero):
        self.numero = numero # numero eh um atributo da classe OrdemServico e eh publico, ou seja, pode ser acessado por outras classes ou objetos fora da classe OrdemServico


    def mostrar_numero(self): # estamos criando uma funcao mostrar_numero com o parametro self como parametro 
        return self.numero


    @classmethod
    def mostrar_empresa(cls): # estamos criando uma funcao mostrar_empresa com o parametro cls como parametro 

        #cls eh uma instancia da classe OrdemServico que significa que estamos criando uma funcao de classe


    @staticmethod
    def validar_numero(numero): #estamos criando uma funcao validar_numero com o parametro numero como parametro
        return numero > 0


    #temos:

    def mostrar_numero(self):
        return self.numero

    #depende de uma instancia da classe OrdemServico

    ordem = OrdemServico(100)


    ordem.mostrar_numero()



    #cls


    @classmethod
    def mostrar_empresa(cls):
        return cls.empresa

    #trabalha com a classe: 


    OrdemServico.mostrar_empresa()

    #staticmethod


    @staticmethod
    def validar_numero(numero):
        return numero > 0

    #nao precisa de : self ou cls


    #so recebe o que realmente precisa:

    OrdemServico.validar_numero(100)

#Uma forma boa de identificar#

## essa funcao precisa saber alguma coisa  sobre um objeto especifico ?

##se sim:
##use self
def metodo(self):
##se nao:
##use cls

@classmethod
def metodo(cls):

##se nao precisa de nada:
##use staticmethod
@staticmethod 
def metodo_valor(valor):
    return valor > 0

#exemplo mais realsita:


class OrdemServico:

    def __init__(self, cliente, cpf):
        self.cliente = cliente
        self.cpf = cpf

        @staticmethod
        def limpar_cpf(cpf): # estamos criando uma funcao limpar_cpf com o parametro cpf como parametro
            return cpf.replace(".", "").replace("-", "") # o que significa replace ? eh uma funcao que substitui um valor por outro

        # return cpf.replace = substitui o valor
        # return cpf.replace(".", "") = substitui o ponto por nada
        # return cpf.replace("-", "") = substitui o traco por nada

        # como isso funciona na pratica = 
        # cpf = 123.456.789-00
        # cpf.replace(".", "") = 12345678900
        # cpf.replace("-", "") = 123456789
        # o que quer dizer ".", "" eh que ele vai substituir o ponto por nada e o que quer dizer "-", "" eh que ele vai substituir o traco por nada
        # o que quer dizer ("-", "") eh que ele vai substituir o traco por nada 

        # como o codigo vai converter de um int para um replace ? 

##PODEMSO FAZXER:

cpf = OrdemServico.limpar_cpf("123.456.789-00")

print(cpf)


##resultado:

12345678900