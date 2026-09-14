vendas = [
    {"cliente": "Ana", "valor": 120},
    {"cliente": "Carlos", "valor": 80},
    {"cliente": "Marcos", "valor": 250},
    {"cliente": "Julia", "valor": 60}
]

def buscar_venda(vendas, cliente_procurado):
    ## puxao de orelha, sempre impor na assinatura ( parametro)
    ## o noome exato do parametro como esta
    ## exemplo, eu coloquei venda, mas o correto é vendas, pŕa receber todo dicionario da lista
#função recebe:
   # vendas
   # cliente_procurado
    for venda in vendas:
        if venda["cliente"] ==  cliente_procurado:
            #cliente_procurado.append(venda)
           return venda
               #estamos retornar uma pessoa especifica com sua chave e valor
               #cliente e valor
               #"venda": venda
               #"cliente_procurado": cliente_procurado
           
    return None

resultado = buscar_venda(vendas, "Marcos")

print(resultado)