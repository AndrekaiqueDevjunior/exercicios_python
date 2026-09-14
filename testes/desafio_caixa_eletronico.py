#Mini-desafio — Caixa Eletrônico

#Você vai criar um programa que simula um caixa eletrônico simples.

#Estado inicial
saldo = 500

#############################
########CAIXA ELETRONICO#####



while True:
    print("1 - CONSULTAR SALDO")
    print("2 - DEPOSITAR")
    print("3 - SACAR")
    print("4 - SAIR")
    print("5 - Histórico ")

    opcao = int(input("Selecione uma opcao: "))
    if opcao == 1:
        print("Você selecionou consultado Saldo: ")
        print(saldo)
        

    if opcao == 2:
        print("Você selecionou Depositar Dinheiro: ")
        print(f"saldo atual", saldo)
        depositar_dinheiro = int(input("Insira o valor que deseja Depositar: "))
        
        # depositar_dinheiro vou adicionar 
        # saldo 500 = valor atual
        saldo += depositar_dinheiro
        # 
        print(f"deposito", depositar_dinheiro)

        print(f"novo saldo", saldo)

        historico.append(depositar_dinheiro)

    if opcao == 3:
        print("Você selecionou Sacar: ")

        sacar_dinheiro = int(input("Insira o Valor que deseja Sacar:  "))
        if sacar_dinheiro > saldo:
            print("Saldo Insuficiente: ")
        else:
            saldo -= sacar_dinheiro
            print(saldo)
            
        historico.append(sacar_dinheiro)
    if opcao == 4:
        print("Você decidiu sair: ")
        print("Obrigado por utilizar o caixa eletrônico! ")
        break

    if opcao == 5:
        print("Você selecionou Histórico: ")

        historico = []


        print(historico)