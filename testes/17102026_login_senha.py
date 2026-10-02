#Crie um programa de login simples.

#O programa deve pedir:

##Usuário:
#Senha:

#@Considere que os dados corretos são:

#Usuário: admin
#Senha: 1234


usuario = input("Insira  o login: ")

senha = input("Insira a senha: ")

if usuario == "admin" and senha == "1234":
    print("Usuario Logado!")
elif usuario == "admin" and senha != "":
    print("Senha Incorreta !")
else:

    print("Usuario Errado! Tenta Novamente Mais tarde")