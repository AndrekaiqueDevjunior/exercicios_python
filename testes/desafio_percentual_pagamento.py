vendas = [
    {"cliente": "Ana", "valor": 120, "pago": True},
    {"cliente": "Carlos", "valor": 80, "pago": False},
    {"cliente": "Marcos", "valor": 250, "pago": True},
    {"cliente": "Julia", "valor": 60, "pago": False},
    {"cliente": "Felipe", "valor": 180, "pago": True}
]

quantidade_total = 0
quantidade_pagas = 0
percentual_pago = 0

for venda in vendas:
    if venda["pago"] == True:

        quantidade_pagas = quantidade_pagas + 1

        quantidade_total = len(vendas)

        percentual_pago = quantidade_pagas / quantidade_total * 100 # é multiplicar por 100, não dividir por 100.


print("quantidade_total: ", quantidade_total)
print("quantidade_pagas: ", quantidade_pagas)
print("percentual_pago", percentual_pago ) 