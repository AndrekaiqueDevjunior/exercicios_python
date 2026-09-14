vendas = [
    {"cliente": "Ana", "valor": 120},
    {"cliente": "Carlos", "valor": 150},
    {"cliente": "Marcos", "valor": 250}
]

def excluir_vendas(vendas, cliente_procurado):


    for venda in vendas:
        if venda["cliente"] == cliente_procurado:
            vendas.remove(venda)### executar


            return vendas
    return None

resultado = excluir_vendas(vendas, "Carlos")
print(resultado)
