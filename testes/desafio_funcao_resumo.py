vendas = [
    {"cliente": "Ana", "valor": 120},
    {"cliente": "Carlos", "valor": 80},
    {"cliente": "Marcos", "valor": 250},
    {"cliente": "Julia", "valor": 60}
]

def gerar_resumo(vendas): # funcao vendas com nome gerar_resumo ( parametro vendas)
    total_vendido = 0 # acumuladores
    quantidade_vendas = 0 #acumuladores

    for venda in vendas: # → pega uma venda por vez.
        total_vendido += venda["valor"] # soma # → soma os valores.

        quantidade_vendas += 1 # contador # → conta quantas vendas existem.

    return { # {total_vendido,quantidade_vendas}

        "total_vendido": total_vendido, #chave : valor
       "quantidade_vendas": quantidade_vendas # chave : valor 
     }

resultado = gerar_resumo(vendas) # resultado pega o resumo do que a função fez.
#Execute gerar_resumo(vendas) e guarde o que ela retornar dentro de resultado. 
print(resultado)
