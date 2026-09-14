vendas = [
    {"cliente": "Ana", "valor": 120, "pago": True},
    {"cliente": "Carlos", "valor": 80, "pago": False},
    {"cliente": "Marcos", "valor": 250, "pago": True},
    {"cliente": "Julia", "valor": 60, "pago": False},
    {"cliente": "Felipe", "valor": 180, "pago": True}
]

total_recebido = 0
quantidade_pagas = 0
total_pendentes = 0
quantidade_pendentes = 0

for venda in vendas:
    if venda["pago"] == True:

        total_recebido += venda["valor"]
        quantidade_pagas += 1
    else:
        total_pendentes += venda["valor"]
        quantidade_pendentes += 1

print("total_recebido", total_recebido )
print("quantidade_pagas", quantidade_pagas)
print("total_pendentes",  total_pendentes)
print("quantidade_pendentes", quantidade_pendentes )