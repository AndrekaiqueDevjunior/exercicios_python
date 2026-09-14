pedidos = [
    {"cliente":"Ana","valor": 120},
    {"cliente":"Carlos","valor": 80},
    {"cliente":"Marcos","valor": 250},
    {"cliente":"Julia","valor": 60},
    {"cliente": "Felipe", "valor": 180}
]

total = 0
pedidos_altos= 0

for pedido in pedidos:
    if pedido["valor"] >=100:
        print(pedido["cliente"], "-" ,"Pedido Alto")
        pedidos_altos = pedidos_altos + 1

    else:
        print(pedido["cliente"], "-" ,"Pedido Normal")


    
    total = total + pedido["valor"]
print("valor total de pedidos:", total)



print("quantidade de pedidos altos: ", pedidos_altos)


