
def fibonacci(posicao):
    if posicao < 0:
        raise ValueError("A posição não pode ser negativa.")

    anterior = 0
    atual = 1

    for i in range(posicao):
        anterior, atual = atual, anterior + atual

    return anterior


posicao = int(input("Digite a posição: "))
print("Número de Fibonacci:", fibonacci(posicao))
