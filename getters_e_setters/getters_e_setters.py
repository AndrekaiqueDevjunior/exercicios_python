#6. getters 

#um getter é um metodo utilizado para consultar um atributo protegido


class OrdemServico:
    def __init__(self, valor: float): # __init__ eh um metodo especial que eh chamado automaticamente quando criamos um objeto da classe, construtor da classe
        #float significa que o atributo valor da classe OrdemServico eh do tipo float e eh publico, ou seja, pode ser acessado 
        # por outras classes ou objetos fora da classe OrdemServico
        self.__valor = valor # self quer dizer: essa classe que estou criando tem esse atributo nome e esse atributo idade tem esse valor

    def get_valor(self) -> float: # get_valor eh um metodo que retorna o valor do atributo protegido __valor
        return self.__valor # 

    def get_status(self) -> str: # get_status eh um metodo que retorna o status do atributo protegido __status
        return self.__status # retorna o status do atributo protegido __status 

#uso:

ordem = OrdemServico(200) # criando um objeto da classe OrdemServico com o valor 200

print(ordem.get_valor()) # chamando o metodo get_valor para obter o valor do atributo protegido __valor
print(ordem.get_status()) # chamando o metodo get_status para obter o status do atributo protegido __status 

#resultado

200 # OrdemServico(200)
ABERTA # = "ABERTA"

#os metodos get_valor() e get_status() permitem ler os dados sem expor diretamente os atributos internos da classe


#Setters
#um setter é um metodo que altera um atributo de maneira controlada
#enquanto o getter permite consultar um atributo, o setter permite alterar um atributo

class OrdemServico:
    def __init__(self, valor: float):
        self.__valor = valor


    def set_valor(self, novo_valor: float) -> None: # o set_valor eh um metodo que recebe um novo_valor do tipo float e nao retorna nenhum valor
        self.__valor = novo_valor # o self.__valor se refere ao atributo protegido __valor da classe, 
        # e estamos atualizando ele com o novo valor passado como parametro do metodo

        self.__valor = novo_valor

#uso correto

ordem = OrdemServico(200) # 

ordem.set_valor(300) # chamando o metodo set_valor para alterar o valor do atributo protegido __valor

#uso Invalido:

ordem.set_valor(-500)

#resultado:

ValueError: O valor nao pode ser negativo.

#O setter não serve apenas para alterar o valor. Ele serve para aplicar regras antes da alteração.

#getter e setter nao precisam existir para tudo

# nao é necessario criar automaticamente:

get_cliente()
set_cliente()
get_numero()
set_numero()
get_descricao()
set_descricao()


#devemos criar metodos quando existe uma necessidade real.
#por exemplo, o status de uma OS, nao deveria sser alterado por um setter generico

ordem.set_status("FINALIZADA")

#é melhor representar as acoes reais do sistema

ordem.finalizar()
ordem.cancelar()

#isso deixa o codigo mais claro e protege melhor as regras de negocio

#9. Encapsulamento com metodos de negocio

# esta é uma vbersao melhor da sua classe:

class OrdemServico: # estamos criando a classe OrdemServico.
    def __init__(
        self,
        numero: int,
        cliente: str,
        descricao: str,
        valor: float,            
    ):
        if valor < 0: #se valor for menor que zero printamos um erro.
            raise ValueError("O valor inicial nao pode ser negativo.") # raise eh usado para lancar um erro. #ValueError eh uma excecao que representa 
                #um erro de valor.
        self.numero = numero
        self.cliente = cliente
        self.descricao = descricao


        self.__valor = valor # observe o self valor esta protegido 
        self.__status = "ABERTA"

    def get_valor(self) -> float: # get_valor eh um metodo que retorna o valor do atributo protegido __valor
        #ESTAMOS ESPERANDO RECEBER VALORES COMO: 3.14 ou 3,14
        return self.__valor # 

    def get_status(self) -> str: # get_status eh um metodo que retorna o status do atributo protegido __status
        # ESTAMOS ESPERANDO RECEBER VALORES COMO: "ABERTA", "FINALIZADA", "CANCELADA"
        return self.__status

    def finalizar(self) -> None: # none eh igual a void em java # -> None significa que o metodo nao retorna nenhum valor
        if self.__status == "CANCELADA" # se o status for CANCELADA printamos um erro 
            raise ValueError("   
                "Uma ordem finalizada nao pode ser cancelada."
            ")

        self.__status = "CANCELADA"

    def aplicar_desconto(self, percentual: float) -> None:
        if self.__status != "ABERTA": # != SIGNIFICA DIFERENTE, LOGO SE O STATUS FOR DIFERENTE DE ABERTA, PRINTAMOS UM ERRO!
            raise ValueError(
                "Só é possivel aplicar desconto em ordens abertas"
            )
        if percentual < 0 or percentual > 100:
            raise ValueError(""
            "Só é possível aplicar desconto em uma  OS ABERTA"
            )

        if percentual < 0 or percental > 100: # se percentual for menor que zero ou maior que 100 printamos um erro:
            raise ValueError((
                "O percentual deve estar entre 0 e 100."
            )

        desconto = self.__valor * percentual / 100 # estamos criando um desconto com base no percentual passado como parametro do metodo 
        #estamos acessando self.__valor que se refere ao atributo protegido __valor da classe e estamos multiplicando ele pelo percentual 
        self.__valor -= desconto # o self.__valor se refere ao atributo protegido __valor da classe, 

        # o que significa -= : estamos subtraindo o desconto do valor da ordem de servico 
        #exemplo: se o valor da ordem de servico for 100 e o desconto for 10, o novo valor da ordem de servico sera 90 

        # e estamos atualizando ele com o novo valor

    def exibir_resumo(self) -> str:
        return(
            f"OS # {self.numero} | "
            f"Cliente: # {self.cliente} | "
            f"Status:  # {self.status} | "
            f"Valor: R$ # {self.valor:.2f} | " # :.2f eh usado para formatar o valor para duas casas decimais 
            #exemplo de valor formatado: 3.14 -> 3.14 ou 3,14 
        )

ordem1 = OrdemServico( # instanciando a classe OrdemServico com os parametros passados como parametros do constructor da classe OrdemServico
    numero=1,
    cliente="André",
    descricao="Formatação de computador",
    valor=200.00
)

print(ordem1.exibir_resumo()) # chamamos o metodo exibir_resumo para exibir o resumo da ordem de servico


#10. o que foi encapsulado ?

#antes
#  self.valor
# self.status


#agora:

self.__valor
self.__status

#esses atributos so devem ser alterados pelos comportamentos da classe:

aplicar_desconto()
finalizar()
cancelar()

#assim a classe protege suas proprias regras.

