
#próximo desafio: agora vamos treinar filtro + menor valor.

vendas = [
    {"cliente": "Ana", "valor": 120, "pago": True},
    {"cliente": "Carlos", "valor": 80, "pago": False},
    {"cliente": "Marcos", "valor": 250, "pago": True},
    {"cliente": "Julia", "valor": 60, "pago": False}, # falso
    {"cliente": "Felipe", "valor": 180, "pago": True}
]

menor_valor = vendas[0]["valor"] ###  vamos começar
### criar uma variavel que recebe a lista vendas
### acessamos a primeira lista que começa por 0 
### o laço de repetição se encarrega de validar com True
### se venda in vendas
#$## acessamos o primeiro item da lista vendas, 
# que é um dicionário, e depois acessamos a chave "valor" desse dicionário.


menor_cliente = vendas[0]["cliente"]

for venda in vendas:
    if venda["pago"] == True:##1. a venda está paga?  " "
        if venda["valor"] < menor_valor:

            #faça
            menor_valor = venda["valor"]

            menor_cliente = venda["cliente"]


print("Menor venda Paga  ", menor_valor )
print("menor cliente: ", menor_cliente )