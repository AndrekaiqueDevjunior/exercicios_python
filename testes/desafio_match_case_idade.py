#idade menor que 12 → "Criança"
#idade de 12 até 17 → "Adolescente"
#idade de 18 até 59 → "Adulto"
#idade 60 ou mais → "Idoso"

idade  = int(input("Digite a sua Idade: "))

match idade:
    case idade if idade < 12: # SE MENOR OU IGUAL 12
        print("Criança")

    case idade if idade >= 12 and idade <= 17:
        print("Adolescente")  
### case idade se idade for maior ou igual 12  E idade for menor ou igual 17
    case idade if idade >= 18 and idade <= 59: #SE MENOR OU IGUAL 18
        print("Adulto")
### case idade se idade for maior ou igual 18  E idade for menor ou igual 59
    case idade if idade >= 60: #SE MAIOR QUE 60 
        print("Idoso")
    case _:
        print("Idade  Nao Registrada")
    