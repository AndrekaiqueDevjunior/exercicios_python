#11 - encapsulamento com @Property

#em python moderno, isso é muito comom usar @property no lugar de getters como:

get_valor()

get_status()

#exemplo>: 

class OrdemServico:
    def __init__(self, valor: float): # __init__ eh um metodo especial que eh chamado automaticamente quando criamos um objeto da classe, construtor da classe
        #float significa que o atributo valor da classe OrdemServico eh do tipo float e eh publico, ou seja, pode ser acessado 
        # por outras classes ou objetos fora da classe OrdemServico
        self.__valor = valor
        self.__status = "ABERTA"

        @property # esse simbolo significa que 
        #@ou seja, pode ser acessado por outras classes ou objetos fora da classe OrdemServico
        def valor(self):
            return self.__valor

        @property
        def status(self) -> str:
            return self.__status


#agora podemos consultar assim:

ordem = OrdemServico(200) # criando um objeto da classe OrdemServico com o valor 200
#podemos ver que Ordem de Servico ficou verde, referente a classe OrdemServico 

#obserrve que nao usamos pareenteses:
ordem.valor # chamando o metodo get_valor para obter o valor do atributo protegido __valor


#isso parec e um atributo comum, mas internamente o python executa: 

@property # Em Python, @property serve para controlar o acesso a um atributo como se ele continuasse sendo uma variável normal.
def valor(self):
    return self.__valor


#Headers: sao metadados da requisicao