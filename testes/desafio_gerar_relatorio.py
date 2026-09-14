pedidos = [
    {"cliente": "Ana", "valor": 120, "status": "pago"},
    {"cliente": "Carlos", "valor": 80, "status": "pendente"},
    {"cliente": "Marcos", "valor": 250, "status": "pago"},
    {"cliente": "Julia", "valor": 60, "status": "cancelado"},
    {"cliente": "Felipe", "valor": 180, "status": "pago"},
    {"cliente": "Rodrigo", "valor": 300, "status": "pago"}
]
def gerar_relatorio(pedidos):
    maior_pedido = 0 # ok 
    quantidade_pagos =0 #Ok
    total_pago = 0 # ok
    media_pago = 0
    maior_cliente = "" #ok
    clientes_pendentes = [] #ok  

    for pedido in pedidos:
        if pedido["status"] == "pago" and pedido["valor"] > maior_pedido:
            # if pedido["status"] == "pago"  #maior_pedido = 0 # ok 
            maior_pedido = pedido["valor"]
            maior_cliente = pedido["cliente"]

        if pedido["status"] == "pago":
            quantidade_pagos += +1 
            # se o status for igual pedido pago +1 pra balança

        if pedido["status"] == "pago":
            total_pago += pedido["valor"]
        
        if pedido["status"] == "pendente":   #clientes_pendentes = [] #ok  
            clientes_pendentes.append(pedido["cliente"])  # acessamos diretamente o cliente que esta com a chave status == pendente 

    media_pago = total_pago / quantidade_pagos

    return {
        "maior_pedido" : maior_pedido,
        "quantidade_pagos" : quantidade_pagos,
        "total_pago" : total_pago,
        "media_pago" : media_pago,
        "maior_cliente" : maior_cliente,
        "clientes_pendentes" : clientes_pendentes
    }

resultado = gerar_relatorio(pedidos) ### variavel resultado que recebe a função gerar_relatorio com argumento ( pedidos )

analise = analisar_relatorio(resultado)

print(analise)

def analisar_relatorio(relatorio):
    #relatorio["total_pago"]

    if relatorio["total_pago"] >= 500:
        return "vendas boas"
    else:
        return "vendas ruins"
    

def classificar_pedido(pedido):

    if pedido["status"] != "pago":
        return "Pedido não pago"
    elif pedido["valor"] >= 200: #entao se
        return "Pedido grande"
    elif pedido["valor"] >= 100: #entao se
        return "Pedido Médio"
    else: #entao 
        return "Pedido Pequeno"



def buscar_maior_pedido(pedidos):

    maior_pedido = None


    for pedido in pedidos:
        #if pedido["valor"] > maior_pedido["valor"]:
        if maior_pedido is None: # se maior_pedido é None
            #"Ainda não tenho nenhum maior pedido."
            maior_pedido = pedido
        elif pedido["valor"] > maior_pedido["valor"]:
            maior_pedido = pedido

    return maior_pedido

# ACESSAR
#pedido["valor"]

# CONTAR
#quantidade_pagos += 1

# ACUMULAR
#total_pago += pedido["valor"]

# ADICIONAR EM LISTA
#clientes_pendentes.append(pedido["cliente"])