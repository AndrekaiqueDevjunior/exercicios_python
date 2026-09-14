####
### Exercício 8 — duas variáveis + condição
###

idade = int(input("Digite a sua idade: "))

tipo = input("Digite o tipo de ingresso: ")


match idade, tipo:
    #idade < 18 + "estudante" → "Meia-entrada"

    case idade,tipo, if idade < 18 and tipo == "estudante": 
        # 
                 ## eu preciso lembrar:
        # "" representa o tipo de ingresso 
        print("Meia entrada [1]")
    #idade >= 18 + "estudante" → "Meia-entrada"
    case idade,tipo, if idade >= 18 and tipo ==  "estudante":
        print("Meia Entrada [2]")


    #qualquer idade + "inteira" → "Ingresso inteiro"
    case _,tipo, if  tipo == "inteira":
        print("Ingresso Inteiro")


    #qualquer outro tipo → "Tipo de ingresso inválido"

    case idade, _,: #     #qualquer outro tipo → "Tipo de ingresso inválido"
        print("tipo de ingresso invalido")

    case idade, _ , if idade == 12 | idade < 12:
        print("entrada gratuita")
          # idade nao pode ser qualquer, precisa ser uma idade
          # abaixo de 12
          # ingresso pode ser qualquer um 
          # por que idade menor que 12 é entrada gratuita 