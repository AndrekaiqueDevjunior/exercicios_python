produtos = [
    {"id": 1, "nome": "Teclado", "preco": 150},
    {"id": 2, "nome": "Mouse", "preco": 80},
    {"id": 3, "nome": "Monitor", "preco": 900},
    {"id": 4, "nome": "Headset", "preco": 200}
]

def buscar_produto(produtos, produto_id):

    for produto in produtos:
        if produto["id"] == produto_id:
            return produto
    return None


def adicionar_produto(produtos, nome, preco):

    novo_id = len(produtos)


    novo_produto = {
        "id": novo_id,
        "nome": nome,
        "preco": preco

    }

    produtos.append(novo_produto)#
    #essa linha diz
    # produto execute a funcao(adicionar ) append usando como argumento novo_produto
    # resumido,  produtos adicione a nova lista de produto


resultado = adicionar_produto(produtos, "monitor", 900)

print(resultado)