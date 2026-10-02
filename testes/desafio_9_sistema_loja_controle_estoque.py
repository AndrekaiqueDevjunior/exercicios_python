produtos = [
    {
        "id": 1,
        "nome": "Teclado",
        "preco": 150,
        "estoque": 5
    },
    {
        "id": 2,
        "nome": "Mouse",
        "preco": 80,
        "estoque": 10
    }
]

{
#====== LOJA ======

#1 - Listar produtos
#2 - Cadastrar produto
#3 - Buscar produto pelo ID
#4 - Realizar venda
#5 - Repor estoque
#6 - Mostrar produtos sem estoque
#7 - Mostrar faturamento
#0 - Sair

#As regras são:
#- Todo produto precisa ter id, nome, preco e estoque.
#- Não permita dois produtos com o mesmo id.
#- Na venda, o usuário informa o id e a quantidade desejada.
#- Não pode vender uma quantidade maior que o estoque.
#- Quando vender, precisa diminuir o estoque.
#- O valor da venda é:
}



while True:

    print(" 1 - Listar produtos " )
    print(" 2 - Cadastrar produto " )
    print(" 3 - Buscar produto pelo ID " )
    print(" 4 - Realizar venda " )
    print(" 5 - Repor estoque " )
    print(" 6 - Mostrar produtos sem estoque " )
    print(" 7 - Mostrar faturamento " )
    print(" 0 - Sair " )

    opcao = int(input("Selecione uma opção: "))

    if opcao == 1:

        def list_products(produtos):
            for produto in produtos:
                print(produto)

        resultado  = list_products(produtos)
        print(resultado)

    if opcao == 2:
        novo_id = len(produtos) + 1
        nome_produto = input("Insira o nome do produto: ")
        preco_produto = int(input("Insira o preço do produto: "))
        estoque_produto = int(input("Insira o tamanho do estoque "))

        def cadastrar_produto(produtos, novo_id, nome_produto,preco_produto,estoque_produto):

            novo_produto = {
                "id": novo_id,
                "nome": nome_produto,
                "preco": preco_produto,
                "estoque": estoque_produto
            }
            produtos.append(novo_produto)

        resultado = cadastrar_produto(produtos, 
                                    novo_id,
                                    nome_produto,
                                    preco_produto,
                                    estoque_produto)
        print(resultado)
        for produto in produtos:
            print(produto)

    if opcao == 3:

        procurar_produto_id = int(input("Insira o ID do produto: "))

        def buscar_produto_id(produtos, procurar_produto_id):
            for produto in produtos:
                if produto["id"] == procurar_produto_id:
                    return produto
            return None

        resultado = buscar_produto_id(produtos, procurar_produto_id)
        print(resultado)

    if opcao == 4:
        
        vender_produto = int(input("Digite o ID do produto: "))

        print("quantos você deseja comprar ?")

        def realizar_venda(produtos, vender_produto):
            quantidade_vendida = int(input("quantos você deseja comprar ?"))
            faturamento = 0
            for produto in produtos:
                if produto["id"] == vender_produto:
                    
                    #quantidade_vendida = int(input("quantos você deseja comprar ?"))

                    if produto["estoque"] >= quantidade_vendida:

                        produto["estoque"] = produto["estoque"] - quantidade_vendida

                        valor_venda = quantidade_vendida * produto["preco"]
                            # 0 = 3 x 80 
                        return valor_venda,produto["estoque"]

                    
                    else:
                        print("Estoque Insuficiente")

                    
                    return faturamento
                
        resultado = realizar_venda(produtos, vender_produto)
        print(resultado)

    if opcao == 5:

        repor_estoque = int(input(" Insira o  id do Pedido que Deseja repor:  "))
        quantidade_repor = int(input("Insira a quantidade que deseja repor: "))

        def repor_estoque_produto(produtos, repor_estoque,quantidade_repor):
            for produto in produtos:
                if produto["id"] == repor_estoque:

                    produto["estoque"] = produto["estoque"] + quantidade_repor

                    return produto
            return None

        resultado = repor_estoque_produto(produtos, repor_estoque,quantidade_repor)
        print(resultado)

    if opcao == 6:

        def produto_sem_estoque(produtos):
            for produto in produtos:
                if produto["estoque"]  <= 0:
                    return produto
            return None

        resultado = produto_sem_estoque(produtos)
        print(resultado)
