contas = [
    {
        "id": 1,
        "titular": "Andre",
        "saldo": 1000.0,
        "ativa": True
    },
    {
        "id": 2,
        "titular": "Maria",
        "saldo": 500.0,
        "ativa": True
    }
]


while True:
    print("1 - LISTAR CONTAS ")
    print("2 - BUSCAR CONTA ")
    print("3 - DEPOSITAR ")
    print("4 - SACAR ")
    print("5 - DESATIVAR CONTA ")
    print("0 - SAIR ")

    opcao = int(input("Selecione uma opção: "))

    if opcao == 1:

        def listar_contas(contas: list) -> list:
            for conta in contas:
                return contas
        resultado = listar_contas(contas)
        print(resultado)

    if opcao == 2:

        conta_id = int(input("Insira o ID da conta que deseja selecionar: "))

        def buscar_contas(contas: list, conta_id: int ) -> dict | None: # dicionario OU nada
            for conta in contas:
                if conta["id"] == conta_id:
                    return conta

        resultado = buscar_contas(contas,conta_id)
        print(resultado)

    if opcao == 3:

        conta_id = int(input("Insira o ID da conta que deseja selecionar: "))
        valor_depositar = float(input("Insira o Valor que deseja depositar: "))

        def depositar_conta(contas: list, conta_id: int,valor_depositar:float) -> dict | None:

            for conta in contas:
                if conta["id"] == conta_id:
                    if valor_depositar <= 0:
                        raise ValueError("valor de deposito inválido")

                    if conta["ativa"] == False:
                        raise ValueError("CONTA INATIVA! IMPOSSIVEL DEPOSITAR" )

                    else:
                        conta["saldo"] += valor_depositar
                    return conta
                
            raise ValueError("Conta não encontrada")
        try:
            resultado = depositar_conta(contas, conta_id,valor_depositar)
            print(resultado)
        except ValueError as erro:
            print(erro)

    if opcao == 4:

        conta_id = int(input("Insira o ID da conta que deseja selecionar: "))
        valor_sacar = float(input("Insira o valor que deseja sacar: "))

        def sacar_conta(contas:list, conta_id: int, valor_sacar:float) -> dict | None:
            for conta in contas:
                if conta["id"] == conta_id:
                    if valor_sacar > conta["saldo"]:
                        raise ValueError("Saldo Insuficiente")

                    if conta["ativa"] == False:
                        raise ValueError("CONTA INATIVA ")
                    
                    #“Se essa regra for quebrada, eu mesmo quero disparar um erro.”
                    
                    conta["saldo"] -= valor_sacar

                    return conta

            return None
        #E o try/except fica fora da função, capturando o erro:
        try:
            resultado = sacar_conta(contas, conta_id, valor_sacar)
        except ValueError as erro:
            print(erro)
           # print(resultado)

    if opcao == 5:

        conta_id = int(input("Insira o ID da conta que deseja desativar: "))

        def desativar_conta(contas: list, conta_id: int) -> dict | None:
            for conta in contas:
                if conta["id"] == conta_id:
                    if conta["ativa"] == False:
                        raise ValueError("Conta já esta desativada")
                    else:
                        conta["ativa"] = False
                    return conta
                
                    ###identação é foda

            raise ValueError("Conta não encontrada")

        try:   
            resultado = desativar_conta(contas, conta_id)
            print(resultado)
        except ValueError as erro:
            print(erro)

            #raise ValueError(...) → dispara o erro
            #except ValueError     → captura o erro