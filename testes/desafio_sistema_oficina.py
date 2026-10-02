servicos = [
    {
        "id": 1,
        "carro": "Citroën C3",
        "servico": "Troca de óleo",
        "valor": 250
    },
    {
        "id": 2,
        "carro": "BMW 320i",
        "servico": "Troca de velas",
        "valor": 600
    }
]


#Seu sistema deverá apresentar este menu:

#===== OFICINA MECÂNICA =====

#1 - Listar serviços
#2 - Buscar serviço pelo ID
#3 - Adicionar serviço
#4 - Atualizar valor do serviço
#5 - Excluir serviço
#6 - Calcular valor total dos serviços
#0 - Sair

#Escolha uma opção:
while True:
    
    print("1 - Listar serviços")
    print("2 - Buscar serviço pelo ID")
    print("3 - Adicionar serviço")
    print("4 - Atualizar valor do serviço")
    print("5 - Excluir serviço")
    print("6 - Calcular valor total dos serviços")
    print("0 - Sair")

    opcao = int(input("Selecione uma opção "))

    if opcao == 1:
            print("Você escolheu  Listar Serviços ")
            print(servicos)


    if opcao == 2:
            print("Você escolheu Buscar Serviço por ID")

            servico_encontrado = int(input("Digite o ID do Serviço: "))

            def buscar_servico(servicos, servico_id):
                for servico in servicos:
                    if servico["id"] == servico_id:
                           return servico
                return None

            resultado = buscar_servico(servicos, servico_encontrado)

            print(resultado)





                   
    if opcao == 3:
            print("Você escolheu  Adicionar Serviço")
            novo_servico = input("Informe o novo serviço: ")
            novo_carro = input("Informe o nome do carro novo: ")
            novo_valor = int(input("Informe o valor do serviço: "))
            
            def  adicionar_servico(servicos,novo_carro, novo_servico,novo_valor):

                adicionar_servico = {
                                "carro": novo_carro,
                                "servico": novo_servico,
                                "valor": novo_valor                          
                            }
                servicos.append(adicionar_servico)
                return servicos
            resultado = adicionar_servico(servicos,
                                          novo_servico,
                                          novo_carro,
                                          novo_valor)
            print(servicos)




    if opcao == 4:
            print("Você escolheu Atualizar Valor do Serviço")
            print("Lista de carros: ")
            for servico in servicos:
                    
                print(servico)

            nome_carro = input("Insira o nome do carro para atualizar: ")
            servico_valor_carro = input("Digite o valor do serviço que deseja atualizada: ")

            def atualizar_servico(servicos,servico_valor_carro,nome_carro):

                for servico in servicos:
                    if servico["carro"] == nome_carro:
                            #se der match
                        servico["valor"] = servico_valor_carro # será inserido o novo valor

                        return servicos
                return None

            resultado = atualizar_servico(servicos,servico_valor_carro, nome_carro)

            for servico in servicos:
                print(servico)

                
    if opcao == 5:
            print("Você escolheu Excluir Serviço")

            for servico in servicos:
                print(servico)
            excluir_carro = input("Insira o nome do Carro: ")
            excluir_servico_carro = input("Insira o serviço que deseja excluir: ")

            def excluir_servico(servicos,excluir_carro,excluir_servico_carro):


                for servico in servicos:
                    if servico["carro"] == excluir_carro and servico["servico"] == excluir_servico_carro:
                        #servico["servico"] == excluir_servico_carro
                        #servico["carro"] == excluir_carro
                        servicos.remove(servico)
                        return servico
                return None

            resultado = excluir_servico(servicos, excluir_carro, excluir_servico_carro)
            print(servico["carro"], excluir_carro)
            print(servico["servico"], excluir_servico_carro)
                
            print(resultado)

            print(servicos)

    if opcao == 6:
            print("Você escolheu Calcular valor total dos serviços ")
            soma = 0
            for servico in servicos:
                valor_servico = servico["valor"]
                soma += valor_servico

            print(soma)
