### Próximo desafio: agora vamos treinar contar vendas por faixa de valor.

vendas = [
    {"cliente": "Ana", "valor": 120},
    {"cliente": "Carlos", "valor": 80},
    {"cliente": "Marcos", "valor": 250},
    {"cliente": "Julia", "valor": 60},
    {"cliente": "Felipe", "valor": 180}
]
###contar vendas logo Contador +1 
vendas_baixas =0
vendas_medias =0
vendas_altas =0

for venda in vendas:
    if venda["valor"] < 100:
      #  vendas_baixas = venda["valor"]
      vendas_baixas += 1

    elif venda["valor"] >= 100 and venda["valor"] < 200:
        #vendas_medias = venda["valor"]
        vendas_medias += 1
    else:
       # venda["valor"] >= 200
        #vendas_altas = venda["valor"]
        vendas_altas += 1

print("vendas Baixas", vendas_baixas)
print("vendas medias ", vendas_medias)
print("vendas altas ", vendas_altas)        
