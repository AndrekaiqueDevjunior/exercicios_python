##2- Uma função recebe por parâmetros uma matriz de entrada, o número de linhas e o
#número de colunas, processa todos os números contando os pares e os ímpares e retorna
#a quantidade do que tiver maior quantidade de ocorrências. Escreva essa função.




def maior_quantidade(matriz, linhas, colunas):
    pares = 0 # é criado a variavel pares que recebe 0 para evitar
    #lixo de memória na hora da soma do resto
    impares = 0 # é criado a variavel impares que recebe 0 para evitar
    # lixo de memória na hora da soma do resto

    for i in range(linhas): # laço que para i no range linhas
        for j in range(colunas): # laço j que serve para repetir um bloco de codigo ou blocos
            # de códigos uma quantidade determinada de vezes
            if matriz[i][j] % 2 == 0: # condição
                # se a matriz i J ter o resto de 2 e for igual a zero
                # some pares = pares + 1 ( 2,4,6,8,10)
                pares += 1
            else: # se entao for impar
                impares += 1 # some impares = impare + 1
                #1,3,5,7,9.....

    return max(pares, impares) # retorne o maximo pares e impares


matriz = [
    [1, 2, 4],
    [3, 6, 8]
]

resultado = maior_quantidade(matriz, 2, 3)
# é criado resultado que vai receber a funcao maior_quantidade
# com parametros da funcao matriz,2 e ,3
print(resultado)
