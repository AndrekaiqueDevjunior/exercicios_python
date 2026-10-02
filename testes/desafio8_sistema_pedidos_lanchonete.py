#====== LANCHONETE ======

#1 - Listar pedidos
#2 - Criar pedido
#3 - Buscar pedido pelo ID
#4 - Finalizar pedido
#5 - Cancelar pedido
#6 - Mostrar faturamento
#7 - Mostrar pedidos em aberto
#0 - Sair


#O id deve ser único.
#Um pedido novo começa com "status": "aberto".
#Não pode finalizar um pedido já finalizado.
#Não pode finalizar um pedido cancelado.
#Não pode cancelar um pedido já finalizado.
#O faturamento deve considerar somente pedidos finalizados.
#O valor de cada pedido deve ser:

###dados iniciais
pedidos = [
{
    "id": 1,
    "cliente": "André",
    "produto": "X-Bacon",
    "quantidade": 2,
    "preco_unitario": 25.00,
    "status": "aberto"
}
]

while True:
    print(" 1 - Listar pedidos " )
    print(" 2 - Criar pedido" )
    print(" 3 - Buscar pedido pelo ID" )
    print(" 4 - Finalizar pedido" )
    print(" 5 - Cancelar pedido" )
    print(" 6 - Mostrar faturamento" )
    print(" 7 - Mostrar pedidos em aberto" )
    print(" 0 - Sair" )
    menu_opcoes = int(input("Selecione uma Opção: "))

    if menu_opcoes == 1:
        def listar_pedidos(pedidos):
            for pedido in pedidos:
                print(pedido)
                return pedido        
            return None
        
        listar_pedidos(pedidos)


    if menu_opcoes == 2:
        novo_id = len(pedidos) + 1
        nome_cliente = input(" Insira o nome do cliente: ")
        produto_lanchonete = input("Insira o produto:  ")
        quantidade_produto = int(input("Insira a quantidade"))
        preco_unitario_pedido = float(input("Insira o preço unitário "))

        def criar_pedido(pedidos,nome_cliente,produto_lanchonete,quantidade_produto
                         ,preco_unitario_pedido):

            novo_pedido = {
                "id": novo_id,
                "cliente": nome_cliente,
                "produto": produto_lanchonete,
                "quantidade": quantidade_produto,
                "preco_unitario": preco_unitario_pedido,
                "status": "aberto"
            }
            pedidos.append(novo_pedido)
            return pedidos
        criar_pedido(pedidos,
                     nome_cliente,
                     produto_lanchonete,
                     quantidade_produto,
                    preco_unitario_pedido
                    )
        for pedido in pedidos:
            print(pedido)


    if menu_opcoes == 3:

        procurar_pedido_id = int(input("Insira o ID do pedido para procurar: "))

        def buscar_pedido(pedidos, procurar_pedido_id):
            for pedido in pedidos:
                if pedido["id"] == procurar_pedido_id:
                    return pedido
                return None

        resultado = buscar_pedido(pedidos, procurar_pedido_id)
        print(resultado)

    if menu_opcoes == 4:

        finalizar_um_pedido = int(input("Insira  o ID do pedido: "))

        def finalizar_pedido(pedidos,finalizar_um_pedido):

            ##aula rapida de == and =

            ## == compara
            ## = altera de status aberto para finalizada(o)

            for pedido in pedidos:


                if pedido["id"] == finalizar_um_pedido and pedido["status"] == "aberto":
                    pedido["status"] = "finalizado"
                    return pedido
                elif pedido["id"] == finalizar_um_pedido and  pedido["status"] == "finalizado":
                    print("Não pode encerrar um pedido já finalizado")
                elif pedido["id"] == finalizar_um_pedido and  pedido["status"] == "cancelado":
                    print("Não pode finalizar um pedido que foi cancelado")

            return None
        resultado = finalizar_pedido(pedidos, finalizar_um_pedido)
        print(resultado)

    if menu_opcoes == 5:

            cancelar_um_pedido = int(input("Insira o Numero do pedido "))

            def cancelar_pedido(pedidos, cancelar_um_pedido):
                for pedido in pedidos:
                    if pedido["id"] == cancelar_um_pedido:
                        pedido["status"] = "cancelado"
                        return pedido
                return None
            resultado = cancelar_pedido(pedidos, cancelar_um_pedido)
            print(resultado)

    if menu_opcoes == 6:
        faturamento = 0
        def calcular_faturamento(pedidos,):
            for pedido in pedidos:
                faturamento = 0
                if pedido["status"] == "finalizado":
                    valor_pedido = pedido["quantidade_produto"] * pedido["preco_unitario_pedido"]

                    faturamento += valor_pedido
            return faturamento


        print(faturamento)

    if menu_opcoes == 7:

        def pedido_in_aberto(pedidos):
            for pedido in pedidos:
                if pedido["status"] == "aberto":
                    return pedido
                return None

        resultado = pedido_in_aberto(pedidos)
        print(resultado)
