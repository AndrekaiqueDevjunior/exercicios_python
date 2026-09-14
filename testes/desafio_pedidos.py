pedidos = [
    {"cliente":"Ana","valor": 120},
    {"cliente":"Carlos","valor": 80},
    {"cliente":"Marcos","valor": 250},
    {"cliente":"Julia","valor": 60},
]
soma = 0
for pedido in pedidos:
    if pedido["valor"] >= 100:
        print(pedido["cliente"], "-" ,"Pedido Alto")
    else:
        print(pedido["cliente"], "-" ,"Pedido Normal")

    soma = soma + pedido["valor"]

print("valor total de todos pedidos:", soma)