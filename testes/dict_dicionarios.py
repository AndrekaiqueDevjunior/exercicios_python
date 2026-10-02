usuario = {
    "nome":"Andre",
    "idade": 27, ## idade nao é uma string que recebe aspas duplas, é um numero INTEIRO, entao nao deve receber aspas duplas
    "cidade": "Sao Paulo",
    "profissao": "Desenvolvedor"
}

print(usuario["nome"])
usuario["idade"] = 28

print(usuario["idade"])
usuario["email"] = "andre@gmail.com"
print(usuario["email"])

for chave in usuario:
    print(chave)

    produto = {
    "nome": "Mouse",
    "preco": 80,
    "estoque": 15
}

for valor in produto.values():
    print(valor)




    produto = {
    "nome": "Monitor",
    "preco": 900,
    "estoque": 5
}

for chave, valor in produto.items():
    if chave == "preco":
        print(valor)