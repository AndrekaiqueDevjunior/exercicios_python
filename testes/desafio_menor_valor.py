pedidos = [
    {"cliente":"Ana","valor": 120},
    {"cliente":"Carlos","valor": 80},
    {"cliente":"Marcos","valor": 250},
    {"cliente":"Julia","valor": 60},
    {"cliente": "Felipe", "valor": 180}
]

menor_valor = pedidos[0]["valor"]
#explicacao antes que eu me esqueça

#@declaramos a variavel menor valor,
# aonde recebe o dicionario pedidos,
# aonde esta o macete, estamos acessando o 
#  primeiro array do dicionario que é a Ana

#  
menor_cliente = ""

for pedido in pedidos: # percorra o laço de pedido em Pedidos
    if pedido["valor"] < menor_valor:
        menor_valor = pedido["valor"]
        menor_cliente = pedido["cliente"]



print("Menor valor", "-", menor_valor)
print("Menor_cliente", "-", menor_cliente)