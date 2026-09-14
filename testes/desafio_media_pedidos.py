pedidos = [
    {"cliente":"Ana","valor": 120},
    {"cliente":"Carlos","valor": 80},
    {"cliente":"Marcos","valor": 250},
    {"cliente":"Julia","valor": 60},
    {"cliente": "Felipe", "valor": 180}
]

total = 0
quantidade = 0
media = 0
#soma = soma + pedido["valor"]

for pedido in pedidos:
    #total vendido
    total  = total + pedido["valor"]
    #quantidade de pedidos
    quantidade = quantidade + 1
    #$media dos pedidos
    media = total / quantidade

print("Total vendido:  ", total)
print("Quantidade de pedidos: ",  quantidade)
print("Média dos Pedidos : ", media)


# outra forma de descobrir quantidade
# quantidade = len(pedidos)