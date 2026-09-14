###inputs

usuario = input("Digite o nome do usuário: ")

senha = input("Digite a senha:: ")


match usuario, senha:
    case "admin", "1234":
        print("Login Realizado")
    case "admin", _:
        print("Senha errada")
    case _,_:
        print("Usuario nao encontrado")
        # foi usado esse método por segurança