usuarios = [
    {
        "id": 1,
        "nome": "Andre",
        "email": "andre@email.com",
        "ativo": True
    },
    {
        "id": 2,
        "nome": "Maria",
        "email": "maria@email.com",
        "ativo": True
    }
]

#====== USUÁRIOS ======

#1 - Listar usuários
#2 - Cadastrar usuário
#3 - Buscar usuário pelo ID
#4 - Desativar usuário
#5 - Ativar usuário
#6 - Buscar usuário pelo email
#0 - Sair

while True:

    print(" 1 - Listar usuários  ")
    print(" 2 - Cadastrar usuário  ")
    print(" 3 - Buscar usuário pelo ID  ")
    print(" 4 - Desativar usuário  ")
    print(" 5 - Ativar usuário  ")
    print(" 6 - Buscar usuário pelo email  ")
    print(" 0 - Sair  ")
    opcao = int(input("Insira uma opção para selecionar: "))


    if opcao == 1:

        def listar_usuarios(usuarios: list) -> list:
                return usuarios
        #“Crie uma função chamada listar_usuarios, que recebe um parâmetro chamado usuarios,
        #  esperado como uma list, e que deve retornar um dict.”
        resultado = listar_usuarios(usuarios)
        print(resultado)

    if opcao == 2:

        novo_id = len(usuarios) + 1
        nome_usuario = input("Insira o nome do usuário: ")
        email_usuario = input("Insira o EMAIL Do usuário: ")
        def cadastrar_usuario(usuarios: list, 
                              novo_id : int,
                              nome_usuario: str,
                              email_usuario: str,
                              
                              ) -> dict: # sera necessário retornar um dicionário
            novo_usuario = {
                    "id": novo_id,
                    "nome": nome_usuario,
                    "email": email_usuario,
                    "ativo": True
                }
            
            usuarios.append(novo_usuario)
            return usuarios
        resultado = cadastrar_usuario(usuarios ,novo_id,nome_usuario,email_usuario )
        print(resultado)

    if opcao == 3:

        usuario_id = int(input("Insira o iD do usuário que deseja executar: "))

        def buscar_usuario_id(usuarios: list, usuario_id: int) -> dict:
            for usuario in usuarios:
                if usuario["id"] == usuario_id:
                    return usuario

        resultado = buscar_usuario_id(usuarios, usuario_id)
        print(resultado)

    if opcao == 4:

        usuario_id = int(input("Insira o ID do usuario que deseja desativar: "))


        def desativar_usuario(usuarios: list,usuario_id:int) -> dict:
            for usuario in usuarios:
                if usuario["id"] == usuario_id:
                    usuario["ativo"] = False
                    return usuario
        resultado = desativar_usuario(usuarios,usuario_id)
        print(resultado)

    if opcao == 5:

        usuario_id = int(input("Insira o ID do usuário que deseja ativar: "))

        def ativar_usuario(usuarios: list, usuario_id: int) -> dict:
            for usuario in usuarios:
                if usuario["id"] == usuario_id:
                    usuario["ativo"] = True
                    return usuario

        resultado = ativar_usuario(usuarios, usuario_id)
        print(resultado)


    if opcao == 6:

        usuario_email = input("insira o email do usuario, para pesquisar: ")

        def buscar_usuario_email(usuarios: list, usuario_email: str ) -> list:
            for usuario in usuarios:
                if usuario["email"] == usuario_email:
                    return usuario

        resultado = buscar_usuario_email(usuarios, usuario_email)
        print(resultado)


    if opcao == 0:
        break