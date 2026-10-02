veiculos = [
    {
        "placa": "ABC1234",
        "modelo": "Citroen C3",
        "entrada": 8,
        "saida": None
    },
    {
        "placa": "DEF5678",
        "modelo": "BMW 320i",
        "entrada": 10,
        "saida": None
    }
]

total_vagas = 5
valor_hora = 10
faturamento = 0

while True:

            print("====== ESTACIONAMENTO ======")

            print("1 - Listar veículos estacionados")
            print("2 - Registrar entrada de veículo")
            print("3 - Registrar saída de veículo")
            print("4 - Buscar veículo pela placa")
            print("5 - Consultar vagas disponíveis")
            print("6 - Calcular faturamento total")
            print("0 - Sair")

            opcao = int(input("Escolha uma opção: ")) 



            if opcao == 1:
                print(" 1 - Listar veículos estacionados ")

                for veiculo in veiculos:
                    print(veiculo)

            if opcao == 2:
                print("2 - Registrar entrada de veículo")

                horario_entrada = int(input("Insira o horário de entrada: "))

                modelo_entrada = input("insira o modelo: ")

                placa_entrada = input("Insira o numero da Placa: ").upper()


                def registrar_entrada(veiculos,placa_entrada,modelo_entrada,horario_entrada):

                    quantidade_suportada = len(veiculos)

                    total_vagas = 5 

                    if quantidade_suportada >= total_vagas:
                        #“A quantidade de veículos já é igual ou maior que a capacidade do estacionamento?”
                        # se a quantidade suporte for maior que 5 
                        #que é o total_vagas =5 
                        # imprimir estacionamento cheio
                        #se o numero de total_vagas for menor que a intenção
                        #de adicionar um novo registro.
                        print("Estacionamento Cheio")   
                        return
                    


                    print(f" Vagas disponíveis {total_vagas}")
                    #Verificar se existem vagas disponíveis.
                    #for veiculo in veiculos:
                    # if veiculo 
                    
                
                    #Impedir a entrada de um veículo cuja placa já esteja 
                    # 
                    #cadastrada no estacionamento.
                    for veiculo in veiculos:
                        if placa_entrada == veiculo["placa"]:
                            print("Essa placa já existe")
                            #menu()
                            return

                    #Adicionar um novo dicionário à lista quando a entrada for permitida.

                    nova_entrada = {       
                        "placa": placa_entrada,
                        "modelo": modelo_entrada,
                        "entrada": horario_entrada,
                        "saida": None

                    }
                    
                    veiculos.append(nova_entrada)
                    total_vagas -= 1
                    #total_vagas = total_vagas -1
                        # Subtrai uma vaga pois um carro entrou
                    print(nova_entrada)


                    
                    return veiculos

                    

                # Verifica se NÃO há mais vagas disponíveis
                    if total_vagas <= 0:
                        print("Estacionamento Cheio!")             
                    #else:
                        #total_vagas -= 1  # Subtrai uma vaga pois um carro entrou
                        #print(f"Nova entrada registrada. Vagas restantes: {total_vagas}")

                registrar_entrada(veiculos,placa_entrada,modelo_entrada,horario_entrada)
               # total_vagas -= 1
                print("Lista Atualizada ")
                for veiculo in veiculos:
                    print(veiculo)

                
            if opcao == 3:
                print("3 - Registrar saída de veículo")

                modelo_saida = input("Insira o modelo: ")
                horario_saida = int(input("Insira o horario de saída: "))


                def registrar_saida(veiculos,modelo_saida,horario_saida):

                    for veiculo in veiculos:
                         if veiculo["modelo"] == modelo_saida:
                              veiculo["saida"] = horario_saida
                              #veiculo["entrada"] = horario_entrada

                              return veiculo
                    return None

                registrar_saida(veiculos,modelo_saida,horario_saida)

                for veiculo in veiculos:

                    #veiculo["entrada"] = horario_entrada

                    tempo_estacionado = horario_saida - veiculo["entrada"]
                    valor_total = tempo_estacionado * valor_hora

                ##faturamento antigo começa com 0 ++
                ## valor pago agora é o valor total 
                ## novo faturamento é somador
                faturamento = faturamento + valor_total
                print(f"Valor Total para Pagar     R${valor_total}")

                quantidade_suportada  = len(veiculos)

                for veiculo in veiculos:
                    if veiculo["modelo"] == modelo_saida:
                        veiculos.remove(veiculo)

                    #if quantidade_suportada <= total_vagas:
                    #    total_vagas += 1


                print(f"total de vagas disponíveis: {total_vagas}")

                print("Lista Atualizada -")
                for veiculo in veiculos:
                    print(veiculo)


                 

            #veiculo.remove(registrar_saida)

            if opcao == 4: 
                print("4 - Buscar veículo pela placa")


                placa_buscar = input("Insira o Numero da placa : ")
                def buscar_placa(veiculos, placa_buscar):
                    for veiculo in veiculos:
                        if veiculo["placa"] == placa_buscar:
                            return veiculo
                    return None

                resultado_busca = buscar_placa(veiculos, placa_buscar)
                print(resultado_busca)

                
            if opcao == 5:
                print("5 - Consultar vagas disponíveis")

                print("total_vagas:", total_vagas)
                print("quantidade veículos:", len(veiculos))
                print("veículos:", veiculos)
                quantidade_veiculos = len(veiculos)

                    #total_vagas = é igual a 5 vagas DISPONIVEIS

                    # len(veiculos) == conta a quantidade de veiculos

                    # 
                vagas_disponiveis = total_vagas - quantidade_veiculos
                    ##quantidade = 5f
                    #soma = 5 - 2 = 3
                   # print(vagas_disponiveis)

                print(vagas_disponiveis) ## deve mostrar 3

                   # print(total_vagas)

            if opcao == 6:


                def calcular_faturamento(veiculos,faturamento,valor_total):

                    print("6 - Calcular faturamento total")
                    faturamento = faturamento + valor_total

                print(faturamento)                    


            if opcao == 0:
                print("Saindo")
                break