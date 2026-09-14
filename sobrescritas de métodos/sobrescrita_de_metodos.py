########### o que é overRide ? ###########


### overide é nada mais que uma classe filha sobrescrever um metodo herdado de uma classe pai


#exemplo:

class Funcionario:
    def trabalhar(self):
        print("Realizando trabalho")





    def trabalhar(self):
        print("Programando")



dev = Desenvolvedor() ## estamos instanciando um objeto da classe Desenvolvedor que herda o metodo trabalhar da classe pai Funcionario


dev.trabalhar() # apontamos um objeto e chamamos a função herdada da classe funcionário que é a classe Pai/Base


# resultado:

## Programando


## A classe Desenvolvedor herdou trabalhar(), mas substituiu o comportamento original.



#O que aconteceu por baixo?

#Temos:

#Funcionario
#│
#└── trabalhar()
  #    "Funcionário trabalhando"


   #    ↑ herança


#Desenvolvedor
#│
#└── trabalhar()
   #   "Desenvolvedor programando"



##macete com super para usar o metodo ou função da classe Pai/ Base = [Funcionário]



class Funcionario:
    def trabalhar(self):
        print("Realizando trabalho")


class Desenvolvedor():

    def trabalhar(self):
        super().trabalhar()#### usando o metodo trabalhar da classe Pai/ Base    
        print("Programando API em Flask")




#vamos instancia dev = Desenvolvedor()

#objeto dev que recebe a classe Desenvolvedor 


dev = Desenvolvedor()

dev.trabalhar()


### exemplo com DOCUMENTOS / ORDEM DE SERVICO / ORDEM DE COMPRA


## IMAGINAMOS UMA CLASSE GENÉRICA CHAMADA DOCUMENTOS QUE TEM UMA FUNCAO BASICA CHASMARADA GERAR RESUMO
## QUE RETORNAA doCUMENTO DO SISTEMA

class Documento: #$## classe base nao usam colchetes, somente classes filhas, pq depende o que vamos fazer com esse método.

    def gerar_resumo(self):

        return "Resumo do Sistema"


class OrdemServico(Documento): ## classe filha herda os atributos e metodos da classe pai Documento


    def gerar_resumo(self):

        return "Resumo da Ordem de Servico"



class OrdemCompra(Documento): ##  classe filha que herda os atributos e metodos da classe pai Documento 


    def gerar_resumo(self): ## pq a função gerar resumo recebe como parametro self ? pq ela eh uma funcao de instancia  

        # que significa que ela recebe um objeto como parametro que eh uma instancia da classe OrdemCompra 

        return "Resumo da Ordem de Compra"



### instanciando esses arrombados filha da puta

os = OrdemServico()
oc = OrdemCompra()


print(os.gerar_resumo())
print(os.gerar_resumo())

## o que caralhos estamos fazendo nessa porra ?
## estamos pela puta que pariu instanciando os arrombados filha da puta que herdam os atributos e metodos da classe pai Documento

## os . quer dizer = essa classe que estou criando tem esse atributo nome e esse atributo idade tem esse valor

## estamos chamando um objeto que eh uma instancia da classe OrdemServico que eh uma instancia da classe Documento

## estamos o gerar_resumo da classe OrdemServico que eh uma instancia da classe Documento

## que no final vai ser

## Resumo da Ordem de Servico

## Resumo da Ordem de Servico


#Perceba algo muito importante:

#O nome do método é igual:

#gerar_resumo()

#mas o comportamento depende do objeto.

#Isso já começa a entrar em polimorfismo.


#Uma regra importante

#Para ser override, normalmente temos:

#Classe pai:

def cancelar(self):
    ...

#Classe filha:

def cancelar(self):
    ...

#O método tem o mesmo nome e representa o mesmo comportamento conceitual, mas a implementação muda.