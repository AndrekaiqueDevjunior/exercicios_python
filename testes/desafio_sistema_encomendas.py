encomendas = [
    {
        "id": 1,
        "cliente": "Andre",
        "origem": "Cangaíba",
        "destino": "Tatuapé",
        "status": "aguardando_motorista",
        "motorista_id": None,
        "valor": 35.00
    },
    {
        "id": 2,
        "cliente": "Carlos",
        "origem": "Penha",
        "destino": "Brás",
        "status": "em_transito",
        "motorista_id": 15,
        "valor": 48.00
    }
]


while True:
    print("1 - Listar Encomendas ")
    print("2 - Buscar Encomendas ")
    print("3 - Aceitar Encomendas ")
    print("4 - Coletar Encomendas ")
    print("5 - Entregar Encomendas ")
    print("6 - contar_por_status ")
    print("7 - calcular faturamento ")
    opcao = int(input("Selecione uma Opção: "))


    if opcao == 1:

        def listar_encomendas(encomendas):
            for encomenda in encomendas:
                print(encomendas)
                return encomenda

        resultado = listar_encomendas(encomendas)

    if opcao == 2:

        procurar_encomendas = int(input("Insira o ID da encomenda: "))
        
        def buscar_encomendas(encomendas,procurar_encomendas):
            for encomenda in encomendas:
                if encomenda["id"] == procurar_encomendas:
                    return encomenda
            return None

        resultado = buscar_encomendas(encomendas,procurar_encomendas)
        print(resultado)

    if opcao == 3:

        escolher_encomenda = int(input("Insira o ID da encomenda que deseja aceitar: "))
        id_motorista = int(input("Insira o ID do motorista:  "))

        def aceitar_encomenda(encomendas,escolher_encomenda,id_motorista):
            for encomenda in encomendas:
                if  encomenda["id"] == escolher_encomenda: 
                    if encomenda["status"] == "aguardando_motorista":
                        encomenda["status"] = "aceita"
                        encomenda["motorista_id"] = id_motorista
                        return encomenda

                    else:
                        print("só pode aceitar com o status 'aguardando motorista' ")
                        return encomenda
                    
            return None

        resultado = aceitar_encomenda(encomendas,escolher_encomenda,id_motorista)
        print(resultado)


    if opcao == 4:

        coletar_por_id = int(input("insira o ID Da encomenda que deseja coletar "))

        def coletar_encomenda(encomendas, coletar_por_id):
            for encomenda in encomendas:
                if encomenda["id"] == coletar_por_id:
                    if encomenda["status"] == "aceita":
                        encomenda["status"] = "em_transito"

                        return encomenda

                    else:
                        print(" O PEDIDO PRECISA ESTAR ACEITA ")


            return None


        resultado = coletar_encomenda(encomendas, coletar_por_id)
        print(resultado)

    if opcao == 5:

        entregar_por_id = int(input("Insira o ID da encomenda que deseja entregar "))

        def entregar_encomenda(encomendas, entregar_por_id):
            for encomenda in encomendas:
                if encomenda["id"] == entregar_por_id:
                    if encomenda["status"] == "em_transito":
                        encomenda["status"] = "entregue"

                        return encomenda

                    else:
                        print(" O STATUS DO PEDIDO PRECISA ESTAR EM: TRANSITO")


            return None
        resultado = entregar_encomenda(encomendas, entregar_por_id)
        print(resultado)

    if opcao == 6:

        def contar_por_status(encomendas):

            contagem_status = {
               "aguardando_motorista": 0,
               "entrega_aceita" : 0,
               "em_transito" : 0,
               "encomenda_entregue": 0

               }
            
            for encomenda in encomendas:
                if encomenda["status"] == "aguardando_motorista":

                    contagem_status["aguardando_motorista"] += 1 
                    
                   # print(f"STATUS : Aguardando motorista {aguardando_motorista} ")
                  #  return encomenda
                
                if encomenda["status"] == "aceita":
                    contagem_status["entrega_aceita"] += 1
                  #  print(f"STATUS : Aguardando motorista {entrega_aceita} ")
                   # return encomenda
                
                if encomenda["status"] == "em_transito":
                    contagem_status["em_transito"] += 1
                 #   print(f"STATUS : Aguardando motorista {em_transito} ")
                  #  return encomenda
                
                if encomenda["status"] == "entregue":
                    contagem_status["encomenda_entregue"] += 1
                 #   print(f"STATUS : Aguardando motorista {encomenda_entregue} ")
                   # return encomenda
            return contagem_status
        
        resultado = contar_por_status(encomendas)
        print(resultado)

    if opcao == 7:
        def calcular_faturamento(encomendas):
            for encomenda in encomendas:
                if encomenda["status"] == "entregue":
                    faturamento += encomenda["valor"]

            return faturamento
        resultado = calcular_faturamento(encomendas)
        print(resultado)
    