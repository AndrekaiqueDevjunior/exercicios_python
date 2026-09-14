###abstract base classe - ABC ###
### classe base abstrata - ABC ###


#vamos importar a biblioteca dela do python 

from abc import ABC, absctractmethod ## importando o modulo abc e o metodo abstractmethod da biblioteca abc


class Pagamento(ABC):
    @absctractmethod
    def processar(self):
        pass

    #qual a finalidade : 
    #processar o pagamento

#agora vamos fazer o Raio - X 

#aqui:

class Pagamento(ABC):

#estamos dizendo:

# pagamento é uma classe abstrata 

#E:

#abstractmethod

## significa:

##esse metodo é obrigatorio para as classes filhas.


##então:

@absctractmethod
def processar(self):
    pass

##define um contrato.


## o que significa contrato ?

## a classe pai esta dizxendo:

## se voce quiser ser um tipo de pagamento, precisa saber processar um pagamento

##entao:

class PagamentoPix(Pagamento):

    def processar(self):
        print("Processando PIX  ")

#esta correto:

#porque PagamrentoPix implementou:


#processar()

## e se eu esquecer ?

class PagamentoCartao(Pagamento):
    pass # quer dizer, nao faça nada




##agora tentamos:


cartao = PagamentoCartao() # estamos criando um objeto cartao que eh uma instancia da classe PagamentoCartao


##python nao permitirá instanciar uma classe.

#porque falta implementar (processar) um metodo na classe PagamentoCartao

#ou seja, o erro aparece antes de começarmos a usar o objeto incorretamente.

#6. a classe abstrata normalmente nao é criada diretamente

# se temos :


class Pagamento(ABC):

    @absctractmethod
    def processar(self):
        pass

#nao devemos fazer:

pagamento = Pagamento() # estamos criando um objeto pagamento que eh uma instancia da classe Pagamento

# por que poagamento represeta uma ideia generica


# o que realmente existe no sistema pode ser:

pix = PagamentoPix() # instanciando o objeto pix que eh uma instancia da classe PagamentoPix 

# ou 

cartao = PagamentoCartao() # instanciando o objeto cartao que eh uma instancia da classe PagamentoCartao


## pense assim:

#'Pagamento
 #  ↓
#conceito geral

#PagamentoPix
#PagamentoCartao
#PagamentoBoleto
 #  ↓
#implementações concretas

### 7. exemplo completo

from abc import ABC, abstractmethod

class Pagamento(ABC):

    @abstractmethod
    def processar(self,valor):
        pass

class PagamentoPix(Pagamento):

    def processar(self,valor): # aqui estamos sobrescrevendo o metodo processar da classe Pagamento. 
        print(f"PIX de R$ {valor}")

class PagamentoCartao(Pagamento):

    def processar(self, valor):
        print(f"Cartão de R$ {valor}")


class PagamentoBoleto(Pagamento):

    def processar(self, valor):
        print(f"Boleto de R$ {valor}") # usamos {} para trazer o valor do parametro valor para dentro da string do print 


#Criamos:

pix = PagamentoPix()
cartao = PagamentoCartao()
boleto = PagamentoBoleto()


## E:

pix.processar(500)
cartao.processar(500)
boleto.processar(500)

## E:

PIX de R$ 500
Cartao de R$ 500
Boleto de R$ 500 


#################codigo##################