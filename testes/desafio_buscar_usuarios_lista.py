#Desafio 3 — Buscar usuários em uma lista
#Nível intermediário

#Considere a seguinte lista de dicionários:

#usuarios = [
 #   {"id": 1, "nome": "André"},
  #  {"id": 2, "nome": "Maria"},
   # {"id": 3, "nome": "Carlos"}
#]

#Crie uma função chamada buscar_usuario() que receba dois argumentos:

#buscar_usuario(usuarios, usuario_id)

#A função deverá percorrer a lista e procurar um usuário pelo seu ID.

#Se encontrar, deverá retornar o dicionário correspondente. Caso contrário, deverá retornar None.
#Conceitos: funções, parâmetros, argumentos, for, dicionários e return.


usuarios = [
    {"id": 1, "nome": "André"},
    {"id": 2, "nome": "Maria"},
    {"id": 3, "nome": "Carlos"}
]

usuario_encontrado = int(input("Digite o ID do usuário: "))

def buscar_usuario(usuarios, usuario_id):

    for usuario in usuarios:
        if usuario["id"] == usuario_id:
            return  usuario
    return None
    #Ele precisa estar fora do for. 
    # Se estiver dentro do for, a função pode retornar None 
    # logo após verificar apenas o primeiro usuário.
resultado = buscar_usuario(usuarios, usuario_encontrado)

print(resultado)