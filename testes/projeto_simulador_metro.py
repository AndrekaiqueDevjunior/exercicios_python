######################################
#####SIMULADOR########################
########DE############################
######METRO###########################

##### 1- VER ESTACOES
##### 2- ENTRAR NO TREM
##### 3 - INICIA VIAGEM
##### 4- SAIR DO TREM
##### 5 - ENCERRAR  


estacoes = [
    {"id": 1, "nome": "Terminal A"}, #0
    {"id": 2, "nome": "Cangaíba"}, # 1
    {"id": 3, "nome": "Penha"},
    {"id": 4, "nome": "Tatuapé"},
    {"id": 5, "nome": "Belém"},
    {"id": 6, "nome": "Mooca"},
    {"id": 7, "nome": "Centro"},
    {"id": 8, "nome": "Terminal B"}
]

entrou_no_trem = False #estados que iniciam falso
viagem_iniciada = False # estados que iniciam falso 
estacao_atual = 1 # ele inicia na estação == id : 1

while True:
        print()
        print("1 - Ver Estações")
        print("2 - Entrar no Trem")
        print("3 - Iniciar Viagem")
        print("4 - Ver Estação Atual")
        print("5 - Sair do Trem")
        print("6 - Encerrar ")


        opcao = int(input("Selecione uma Opção: "))
        print()
        if opcao == 1:
            for estacao in estacoes:
                print(estacao)


        if opcao == 2:
            pergunta = input("Deseja Entrar no Trem ?: ")

            if pergunta.lower() == "sim":
                #estou usando lower pra nao ter limitação de 
                #maiusculo ou minusculo
                #entrou no trem iniciada com falsa = entao nao estou dentro do trem
                #se eu digitar sim estou [dentro_do_trem] = logo True
                entrou_no_trem = True

                print("entrou no trem")
            else:
                print("Ainda na estação ")

        if opcao == 3: # se entrou no trem, mantem como True = logo dentro da caixinha [trem]

            if  entrou_no_trem == False:
                print("Você precisa entrar no Trem para Desembarcar")
                

            else: # logo precisa ser TRUE
                    

                    #estacao atual é um numero variavel iniciada como =2 [cangaiba]
                    #    
                while entrou_no_trem: ## enquanto entrou no trem for verdadeiro, pois ele inicia como False, logo entrar no trem o torna TRUE
                        #TRUE
                        estacao_agora = estacoes[estacao_atual]
                        #estacao_atual = INT NUMERAL 0,1,2,3
                        #estacao_agora = string
                        # estacoes = lista
                        # estacao[estacaoatual]
                        #estacao atual acessa o numero da lista desejado
                        
                        desembarque_pergunta = input(f"deseja Desembarcar Neste Trem ?: {estacao_agora["nome"]} ")
                        #porque estacao_agora é o dicionário, enquanto estacao_atual é o índice numérico.
                        if desembarque_pergunta.lower() == "sim":
                              #  desembarque_pergunta = input(f"deseja Desembarcar Neste Trem ?: {estacao_agora["nome"]} ")
                                ###   porque estacao_agora é o dicionário, 
                                # enquanto estacao_atual é o índice numérico.
                                    ###: estacao_atual precisa mudar quando o trem avança.
                                entrou_no_trem = False
                                print(f"Saindo de: {estacao_agora['nome']} " )
                                print(" Desembarcou! ")

                        elif desembarque_pergunta.lower() == "nao":
                                estacao_atual += 1 # pula pra proxima estação 

                                estacao_agora = estacoes[estacao_atual]
                                print(estacao_agora["nome"])
                            # entrou_no_trem = True ## nao precisamos desse estado porque enquanto nao mudar o estado
                            # ele permanece  verdadeiro
                                print("Ainda no Trem")
                        



        if opcao == 4: 
        #    print("4 - Ver Estação Atual")
            ver_estacao_atual = estacoes[estacao_atual]
            print(f"Estação Atual: {ver_estacao_atual["nome"]}") 

        if opcao == 5:
            if entrou_no_trem == True:
                print("Você Saiu do Trem")


            if entrou_no_trem == False:
                print("Você Ainda Não Entrou no trem")