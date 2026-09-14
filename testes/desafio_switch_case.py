#=== MENU ===
#1 - Cadastrar produto
#2 - Listar produtos
#3 - Buscar produto
#4 - Sair

#Escolha uma opção:


opcao = int(input("Selecione uma opcao: "))


match opcao:
    case 1:
        print("Cadastrar Produto")
    case 2:
        print("Listar Produto")

    case 3:
        print("Buscar")
    case 4:
        print("Sair")
    case _:
        print("Opcao invalida ")
