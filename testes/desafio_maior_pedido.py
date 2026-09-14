pedidos = [
    {"cliente":"Ana","valor": 120},
    {"cliente":"Carlos","valor": 80},
    {"cliente":"Marcos","valor": 250},
    {"cliente":"Julia","valor": 60},
    {"cliente": "Felipe", "valor": 180}
]

maior_valor = 0
maior_cliente = ""

for pedido in pedidos:
    if pedido["valor"] > maior_valor:
        maior_valor = pedido["valor"]
        maior_cliente = pedido["cliente"]
      #maior_valor = pedido["valor"] + pedido["valor"]
    else:
        pass
#if  pedido["valor"] > maior_valor:
#   print("Maior Cliente", maior_valor)

print("maior valor", "-", maior_valor)
print("maior_cliente:", "-", maior_cliente)
