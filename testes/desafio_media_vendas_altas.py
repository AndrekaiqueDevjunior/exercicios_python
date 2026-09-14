######
###### 
###### 
###Próximo desafio: agora vamos juntar contador + acumulador + média por faixa.
vendas = [
    {"cliente": "Ana", "valor": 120},
    {"cliente": "Carlos", "valor": 80},
    {"cliente": "Marcos", "valor": 250},
    {"cliente": "Julia", "valor": 60},
    {"cliente": "Felipe", "valor": 180},
    {"cliente": "Rodrigo", "valor": 300}
]

#valor>=200.

quantidade_vendas_altas = 0
total_vendas_altas = 0
media_vendas_altas = 0

for venda in vendas:
    if venda["valor"] >= 200:


        quantidade_vendas_altas += 1 # se a a venda ter o valor maior ou igual á 200
        # soma +1 # quantidade == contar 
        total_vendas_altas += venda["valor"]
        # total_vendas_altas = total_vendas_altas +  venda["valor"]
        # laço corre, achou um valor acima de 200? +1
        # laço corre, achou um valor acima de 200 ? +1
        
media_vendas_altas = total_vendas_altas/quantidade_vendas_altas



print("quantidade_vendas_altas: ", quantidade_vendas_altas )
print("total_vendas_altas: ", total_vendas_altas  )
print("Media_vendas_altas: ", media_vendas_altas )

#For precorre
#if Filtragem
#+= 1 Conta+1
#+= valor -> acumula

#depois do for -> calcule a média 