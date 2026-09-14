###desafio_funcao_vendas.py

vendas = [
    {"cliente": "Ana", "valor": 120},
    {"cliente": "Carlos", "valor": 80},
    {"cliente": "Marcos", "valor": 250},
    {"cliente": "Julia", "valor": 60}
]



#resultado = 0
def calcular_total(vendas):

    total = 0
    for venda in vendas:
        total += venda["valor"]

    return total 
    
resultado = calcular_total(vendas) # variavel resultado recebe calcular total
        # argumento (vendas)

print(resultado)



