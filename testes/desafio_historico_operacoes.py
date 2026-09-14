# Estação atual: Cangaíba

# 1 - Avançar para próxima estação
# 2 - Voltar para estação anterior
# 3 - Mostrar histórico
# 4 - Sair

estacoes = [
    "Cangaíba",  # 0
    "Penha",     # 1
    "Tatuapé",   # 2
    "Belém",     # 3
    "Brás"       # 4
]

avancar_estacao = 0
voltar_estacao = 0
estacao_atual = 0
historico = []


while True:

    print()

    print("1 - Avançar para a próxima estação")
    print("2 - Voltar para a estação anterior")
    print("3 - Mostrar Histórico")
    print("4 - Sair")

    opcao = int(input("Selecione uma opção: "))

    if opcao == 1:

        print("Opção 1 selecionada")

        while True:

            avancar_estacao_pergunta = input(
                "Deseja Avançar para a próxima Estação? : "
            )

            if avancar_estacao_pergunta.lower() == "sim":

                if estacao_atual != len(estacoes) - 1:
                    #print(f"Você está em: {estacao_agora}")

                    estacao_atual += 1
                    estacao_agora = estacoes[estacao_atual]
                    
                    
                    
                    print(f"Chegamos na estação {estacao_agora}")

                    print("Índice atual:", estacao_atual)
                    print("Tamanho da lista:", len(estacoes))
            

                else:

                    break

            if avancar_estacao_pergunta.lower() == "nao":

                #len(estacoes) - 1

                print(estacao_agora)

                break
            historico.append(estacao_agora)

        if estacao_agora == 5:
            print("Você chegou a estação FINAL")

    if opcao == 2:

        print("Você escolheu Voltar estação Anterior")

        while True:

           


            pergunta_voltar_estacao = input(
                "Você deseja voltar uma estação: ? "
            )

            if pergunta_voltar_estacao == "sim":
               # print(f"Estação Atual : {estacao_anterior}")
                if estacao_atual != 0:
                    ## se a estação atual nao for 0
                    ## pode diminuir
                   # print(f"Estação Atual : {estacao_anterior}")

                    estacao_atual -= 1
                    estacao_anterior = estacoes[estacao_atual]
                    print(f"Da estação: {estacao_agora} você está em: ")
                    print(estacao_anterior)
                    historico.append(estacao_anterior)

                if estacao_atual == 0:
                    print("Você voltou para o começo ")
                    break

               # else:
                    #break

    if opcao == 3:

        print("Você escolheu o Histórico")

        print(historico)