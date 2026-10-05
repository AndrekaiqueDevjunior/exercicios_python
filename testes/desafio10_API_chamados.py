chamados = [
    {
        "id": 1,
        "titulo": "Computador não liga",
        "usuario": "Carlos",
        "prioridade": "alta", # baixa, média, alta
        "status": "aberto" ##fechado
    },
    {
        "id": 2,
        "titulo": "Internet lenta",
        "usuario": "Ana",
        "prioridade": "media",
        "status": "fechado"
    }
]

{
#1 - LISTAR CHAMADO
#2 - BUSCHAR CHAMADO
#3 - CRIAR CHAMADO
#4 - ATUALIZAR_STATUS
#5 - EXCLUIR CHAMADO
#6 - FILTRAR POR STATUS
#7 - SAIR
}

while True:
    print("1 - LISTAR CHAMADO ")
    print("2 - BUSCHAR CHAMADO")
    print("3 - CRIAR CHAMADO ")
    print("4 - ATUALIZAR_STATUS ")
    print("5 - EXCLUIR CHAMADO ")
    print("6 - FILTRAR POR STATUS ")
    print("7 - CONTAR POR STAATUS ")

    opcao = int(input("Selecione uma opção: "))

    if opcao == 1:


        def listar_chamados(chamados):
            for chamado in chamados:
                print(chamado)
        listar_chamados(chamados)

    if opcao == 2:
        chamado_procurar = int(input("Insira o ID do pedido: "))
        def buscar_chamado(chamados, chamado_procurar):
            for chamado in chamados:
                if chamado["id"] == chamado_procurar:
                    return chamado
            return None
        
        resultado = buscar_chamado(chamados,chamado_procurar)
        print(resultado)

    if opcao == 3:

        id_novo = len(chamados) + 1
        titulo_novo = input("Insira o Titulo do chamado: ")
        usuario_novo = input("Insira o Usuário Novo: ")
        prioridade_nova = input(" Insira a prioridade nova: ")
        status_novo =  input("Insira o Status novo: ")##aberto,fechado

        def criar_chamado(chamados,id_novo,titulo_novo,usuario_novo,prioridade_nova,status_novo):


            novo_chamado = {
                "id": id_novo,
                "titulo": titulo_novo,
                "usuario": usuario_novo,
                "prioridade": prioridade_nova, # baixa, média, alta
                "status_novo": status_novo #aberto, fechado
            }
            chamados.append(novo_chamado)
            return chamados

        resultado = criar_chamado(chamados,id_novo,titulo_novo,usuario_novo,prioridade_nova,status_novo)
        print(resultado)

    if opcao == 4:

        procurar_chamado = int(input("Insira o  ID do chamado: "))
        atualizar_status = input("Atualize o STATUS: ")

        def atualizar_status_por_id(chamados, atualizar_status,procurar_chamado):
            for chamado in chamados:
                if chamado["id"] == procurar_chamado:
                    chamado["status"] = atualizar_status
                    return chamados
            return None
        resultado = atualizar_status_por_id(chamados, atualizar_status,procurar_chamado)
        print(resultado)

    if opcao == 5:

        excluir_chamado_id = int(input("Insira o ID que deseja excluir: "))


        def excluir_chamado(chamados,excluir_chamado_id):
            for chamado in chamados:
                if chamado["id"] == excluir_chamado_id:
                    chamados.remove(chamado)
                    print(f"chamado excluído: {chamado}")
                    return chamados
            return None

        resultado = excluir_chamado(chamados, excluir_chamado_id)
        print(resultado)

    if opcao == 6:

        print("1- ABERTO ")
        
        print("2- FECHADO")
        opcao_filtro = int(input("Digite o Numero do Filtro: "))

        def filtrar_por_status(chamados, opcao_filtro):
            for chamado in chamados:
                if opcao_filtro == 1 and chamado["status"] == "aberto":
                    print(chamado)
                if opcao_filtro == 2 and chamado["status"] == "fechado":
                    print(chamado)
            return 

        resultado = filtrar_por_status(chamados, opcao_filtro)
        print(resultado)

    if opcao == 7:

        def contar_por_status(chamados):
            chamado_aberto = len(chamados)
            chamado_fechado = len(chamados)


            for chamado in chamados:
                if chamado["status"] == "aberto" :

                    chamado_aberto = +1
                    print(f"Chamados aberto:{chamado_aberto} ")
            
                if chamado["status"] == "fechado":

                    chamado_fechado = +1
                    print(f"Chamados fechado:{chamado_fechado} ")
            return chamado_aberto,chamado_fechado

        resultado = contar_por_status(chamados)
        print(resultado)

    if opcao == 8:

        buscar_usuario = input("Insira o nome do usuário: ")

        def buscar_por_usuario(chamados,buscar_usuario):
            for chamado in chamados:
                if chamado["usuario"] == buscar_usuario:
                    print(chamado)
                    return chamados

        resultado = buscar_por_usuario(chamados,buscar_usuario)