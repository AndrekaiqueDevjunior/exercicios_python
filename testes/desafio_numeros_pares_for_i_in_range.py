####

#Exercício 2 — Números pares
#for i in range(1,20+1):
 #   if i % 2 == 0:
  #      print(i)


#exercicio - soma
#soma = 0
#for i in range (1,10+1):
 #   soma += i

#print(soma)

#exercício 4 - tabuada
#soma = 0
#numero = int(input("Digite um numero: "))

#for i in range(1, 10+1):

 #   soma = numero * i
  #  print(f"")
   # print(f" {numero} x {i}  =   {soma}")

#numeros = []
#soma = 0

#matriz = []
#for i in range (1,4+1):
#for linha in matriz:
 # linha = []
  #for j in range(1,4+1):
   # valor = linha+numeros
    #soma = i+j
    #linha.append(soma)
  #matriz.append(linha)


soma =0
#print(f" {matriz}" ,end="\n")
matriz = [
    ["André", 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for linha in matriz: # # percorre as linhas
    for numero in linha: #  # percorre os números da linha
      soma += numero

      print(numero , end=" + ")
    print() #  # terminou a linha → quebra de linha
#print(soma)
print(soma)
