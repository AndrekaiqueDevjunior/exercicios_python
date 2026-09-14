vendas = [
    {"cliente": "Ana", "valor": 120},
    {"cliente": "Carlos", "valor": 80},
    {"cliente": "Marcos", "valor": 250}
]

def atualizar_venda(vendas, cliente_procurado, novo_valor): # < -  argumentos ( parametros )


#  novo_valor =  {
#  "nome": "Carlos",
#  "valor": 80
#   }

    for venda in vendas:
        if venda["cliente"] == cliente_procurado: # se venda 

            venda["valor"] = novo_valor

            return vendas
    return None

resultado = atualizar_venda(vendas, "Carlos", 150)
#engraçado como funciona a receita do python
# criamos uma funcao e passamos toda logica
# criamos o resultado

print(resultado)

####“Execute a função atualizar_venda, passando a lista vendas, procurando "Carlos"
#  e usando 150 como novo valor. 
# Depois, pegue o que a função retornar e guarde dentro de resultado.”