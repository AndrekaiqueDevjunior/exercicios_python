carros = [

    {"nome": "Citroen C3 1.6 16v", "servico": "troca de oleo"},
    {"nome": "Palio 1.0 8v", "servico": "Troca de liquido de arrefecimento"}
    
]
carro_novo = input("Digite o nome do carro: ")
servico_novo = input("Digite o nome do servico: ")

def adicionar_carro(carros,carro_novo,servico_novo):

    #carro_novo = input("Digite o nome do carro")
    #servico_novo = input("Digite o nome do servico")

    novo_carros = {
        "nome": carro_novo,
        "servico": servico_novo
    }

    carros.append(novo_carros)
    return carros
print(carros)
