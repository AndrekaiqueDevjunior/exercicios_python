#@Crie um match/case que responda:

#$200 → "OK"
#201 → "Criado"
#400 → "Requisição inválida"
#401 → "Não autorizado"
#404 → "Não encontrado"
#500 → "Erro interno do servidor"
#qualquer outro → "Status desconhecido"

opcao  =  int(input("DIgite o STATUS HTTP: "))

match opcao:
    case 200:
        print(" OK ")

    case 201:
        print("Criado")
    case 400 | 401 | 403 | 404 :
        print(" Erro de cliente ")
    case 500 | 502 | 503:
        print(" Erro do Servidor ")
    case _:
        print("Status desconhecido")