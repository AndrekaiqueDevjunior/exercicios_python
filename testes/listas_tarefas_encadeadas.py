from dataclasses import dataclass


@dataclass
class regItem:
    item: str
    prox: int

listaTarefas = [
                regItem('Efetuar um Saque no caixa automatico',5),
                regItem('comprar livros na livraria',3),
                regItem('Deixar o Carro no estacionamento', 7),
                regItem('Pegar as roupas na lavanderia', -1),
                regItem('Buscar encomendas no correio', 0),
                regItem('comprar presente na loja de brinquedos', 1),
                regItem('Autenticar documentos no cartório', 4),
                regItem('Comprar calçados no shopping', 6)

]

começo = 2 # começo da lista, primeira tarefa

tarefa = listaTarefas[começo] # criando a variavel tarefa   que recebe a listaTarefas com o argumento começo
i=1
print(f'Tarefa {i}: {tarefa.item}')
while tarefa.prox !=  -1: #$ enquanto a proxima terefa for diferente  -1
    i += 1
    tarefa = listaTarefas[tarefa.prox]
    print(f'tarefa {i}: {tarefa.item}')
# esse exercicio ele pega umma lista de tarefa e deixa ela organizada, enviando o -1 para o ultimo item da lista 