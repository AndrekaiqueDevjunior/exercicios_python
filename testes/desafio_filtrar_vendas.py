vendas = [
    {"cliente": "Ana", "valor": 120},
    {"cliente": "Carlos", "valor": 80},
    {"cliente": "Marcos", "valor": 250},
    {"cliente": "Julia", "valor": 60}
]

#Objetivo: retornar uma nova lista contendo apenas vendas com valor maior
#  ou igual ao valor_minimo.
valor_minimo=100

def filtrar_vendas(vendas, valor_minimo):
    nova_vendas = []

    for venda in vendas: 
        if venda["valor"] >= valor_minimo:
            nova_vendas.append(venda)
            #estou adicionando o valor da venda que passar do valor minimo que é 100
            # sem misterio
            #lista vazia que vai guardar = nova_vendas = []
            # percorre o laço
            # se venda (valor for minimo) = adicione na nova lista 


    return {
        "valor_minimo" : valor_minimo,
        "nova_vendas" : nova_vendas
    }

resultado = filtrar_vendas(vendas,valor_minimo)

print(resultado)