vendas = [
    {"cliente": "Ana", "valor": 120},
    {"cliente": "Carlos", "valor": 80},
    {"cliente": "Marcos", "valor": 250},
    {"cliente": "Julia", "valor": 60},
    {"cliente": "Felipe", "valor": 180}
]

total_vendas_baixas = 0
total_vendas_medias = 0
total_vendas_altas = 0

for venda in vendas: 
    if venda["valor"] < 100: # → soma o dinheiro das vendas abaixo de 100.
        total_vendas_baixas  += venda["valor"]

    elif venda["valor"] >= 100 and venda["valor"] < 200: # → soma o dinheiro das vendas entre 100 e 199.
        total_vendas_medias += venda["valor"]

    else: # → soma o dinheiro das vendas de 200 pra cima.
        total_vendas_altas += venda["valor"]

print("total_vendas_baixas", total_vendas_baixas)
print("total_vendas_medias", total_vendas_medias)
print("total_vendas_altas ", total_vendas_altas)