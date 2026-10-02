#Crie um programa que:

#Peça o nome do usuário.
#Peça a idade.
#Peça a cidade.


nome_user = input("Insira um nome de usuario: ")

age_user = int(input("Insira a idade: "))

city_user = input("Insira a cidade: ")

print(f"Olá, {nome_user}, você tem {age_user} anos, e mora em {city_user}")

if age_user >= 18:
    print(f"Você é Maior de idade: {age_user}")
else:
    print("Você é menor de idade")

    