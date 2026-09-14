clientes = [
    {"nome": "Ana", "Ativo": True},
    {"nome": "André", "Ativo": False},
    {"nome": "Kauê","Ativo": True},
    {"nome": "Rodrigo","Ativo": False}

]

for cliente in clientes:
    if cliente["Ativo"] == True:
        print(cliente["nome"], "-", "Cliente Ativo")
    else:
        print(cliente["nome"], "-", "Cliente Desativado/Inativo") 