vendas = [
    {"cliente": "Ana", "valor": 120, "pago": True},
    {"cliente": "Carlos", "valor": 80, "pago": False},
    {"cliente": "Marcos", "valor": 250, "pago": True},
    {"cliente": "Julia", "valor": 60, "pago": False},
    {"cliente": "Felipe", "valor": 180, "pago": True}
]

total_recebido = 0
total_pendente = 0


for venda in vendas:
    if venda["pago"] == True:

        total_recebido += venda["valor"]

    else:
        total_pendente += venda["valor"]

         
print("Total Recebido: ", total_recebido)  
print("Total Pendente: ", total_pendente)