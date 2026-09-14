##=== MENU HTTP ===
#1 - GET - LER
#2 - POST - ENVIAR
#3 - PUT - ATUALIZAR
#4 - DELETE  - DELETAR

opcao = input("Selecione um Método HTTP: ")


match opcao:
    case "GET":
        print("Buscando Dados")
    case "POST":
        print("Criando Dados")
    case "PUT":
        print("Atualizando Dados...")
    case "DELETE":
        print("Deletando Dados...")
    case _:
        print("Metodo Inválido ou nao existe")
 