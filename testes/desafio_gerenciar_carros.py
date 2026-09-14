###===OFICINA PINDAMONHAGABA===####
# 1 - LER CARROS
# 2 - ADICIONAR CARRO 
# 3 - ATUALIZAR CARRO
# 4 - DELETAR CARRO


carros = [

    {"id": 1, "nome_carro": "Citroen C3 1.6 16v", "servico_carro": "troca de oleo"},
    {"id": 2, "nome_carro": "Palio 1.0 8v", "servico_carro": "Troca de liquido de arrefecimento"}
    
]

while True:# enquanto for verdadeiro
    print("1 - LER CARROS")
    print("2 - ADICIONAR CARRO") 
    print("3 - ATUALIZAR CARRO") 
    print("4 - DELETAR CARRO")


    gerenciar_oficina = int(input("Selecione uma Opção: "))



    match gerenciar_oficina:

                case 1:

                    for carro in carros:
                                                print(f"Carro: {carro['nome_carro']}")
                                                print(f"Servico: {carro['servico_carro']}")
                                                print()
                    
                    def ler_carros(carros):
                        for carro in carros:
                            print(f"Carro: {carro['nome_carro']}")
                            print(f"Servico: {carro['servico_carro']}")
                            print()


                case 2:
                    print("Vocẽ selecionou ADICIONAR CARRO - OPÇÃO 2")
                    nome_carro = input("insira o nome do carro: ")
                    servico_carro = input("Insira o nome do serviço que irá fazer: ")


                    def adicionar_carro(carros, nome_carro,servico_carro): # Isso apenas define a função.
                        # Dentro de adicionar_carro(), você deverá pedir:

                       


                        novo_carro = {
                            "nome_carro": nome_carro,
                            "servico_carro": servico_carro
                        }

                        carros.append(novo_carro)

                        print(novo_carro)
                        return carros
                    
                    adicionar_carro(carros,nome_carro,servico_carro)

            
                    #resultado = adicionar_carro(carros, "Golf GTI","Troca de Bico Injetores" )
                    print("Lista Atualizada ")
                    for carro in carros:
                        print(carro)






                case 3:

                    print("Você selecionou ATUALIZAR CARRO - OPÇÃO 3")
                    print("Lista de carros: ")
                    for carro in carros:
                    
                        print(carro)
                   
                    nome_carro = input("Insira o nome do carro para atualizar: ")
                    servico_carro = input("Insira o nome do serviço para atualizar: ")



                    def atualizar_carro(carros,nome_carro ,servico_carro):

                        for carro in carros:
                            if carro["nome_carro"] == nome_carro: # aqui procura pelo carro 
                                carro["servico_carro"] = servico_carro # aqui inserimos o novo servico

                                return carro
                        #return None
                    atualizar_carro(carros, nome_carro, servico_carro)

                   # resultado = atualizar_carro(carros, "Palio 1.0 8v", "Limpeza velas de admissão ")
                    for carro in carros:
                        print(carro)

                    ### ==  → comparação
                     ###  =   → atribuição


                case 4:
                    for carro in carros:

                        print(carro)
                    carro_remover = input("Digite o nome do carro que quer apagar: ")

                    def excluir_carro(carros, carro_remover):

                        for carro in carros:
                            if carro["nome_carro"] == carro_remover:

                                carros.remove(carro)

                    excluir_carro(carros,carro_remover)

                    for carro in carros:
                    
                        print(carro)
