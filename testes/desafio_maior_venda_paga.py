##
## Seu objetivo é descobrir qual foi a maior venda entre as vendas pagas.
##
vendas = [
    {"cliente": "Ana", "valor": 120, "pago": True},
    {"cliente": "Carlos", "valor": 80, "pago": False},
    {"cliente": "Marcos", "valor": 250, "pago": True},
    {"cliente": "Julia", "valor": 60, "pago": False},
    {"cliente": "Felipe", "valor": 180, "pago": True}
]
maior_valor =0 
maior_cliente = ""
for venda in vendas:
    if venda["pago"] == True:
        if venda["valor"] > maior_valor:
            maior_valor = venda["valor"]
            maior_cliente = venda["cliente"]


print(" maior venda", maior_valor )
print(" maior cliente", maior_cliente )