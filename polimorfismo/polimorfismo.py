###########usando o polimorfismo na pratica###########


##podemos criar:


class Pagamento:

    def processar(self, valor):
        print("Processando pagamento")

class PagamentoPix(Pagamento):

    def processar(self,valor):
        print(f"Processando Pix de R${valor}")


class PagamentoCartao(Pagamento):

    def processar(self, valor):
        print(f"Cobrando R$ {valor} no cartao ") # usamos {valor} para que o valor seja formatado para duas casas decimais


class PagamentoBoleto(Pagamento):

    def processar(self, valor):

        print(f"Gerando Boleto de R${valor}") # F significa formatar para que o valor seja formatado para duas casas decimais 
        #exemplo: se o valor for 100, ele vai ser formatado para 100.00





def realizar_pagamento(pagamento, valor): ## aqui estamos criando uma funcao que recebe um pagamento e um valor
    pagamento.processar(valor) ## o parametro pagamento recebe um pagamento, e o valor recebe um valor



## agora:

pix = PagamentoPix()
cartao = PagamentoCartao()
boleto = PagamentoBoleto()


## vamos aproveitar a funcao realizar_pagamento para realizar pagamentos via pix, cartao e boleto

## centralizando uma funcao.

realizar_pagamento(pix, 500)
realizar_pagamento(cartao, 500)
realizar_pagamento(boleto, 500)