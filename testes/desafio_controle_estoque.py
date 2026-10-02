#Seu programa deverá:

#Mostrar o nome, o preço e a quantidade em estoque. ok

#Solicitar ao usuário quantas unidades deseja comprar. ok

#Verificar se existe estoque suficiente.

#Se houver estoque, subtrair a quantidade comprada.

#Se não houver, exibir "Estoque insuficiente!".

produto = {
    "nome": "Teclado",
    "preco": 150,
    "estoque": 8
}



print(produto)

add_estoque = int(input("Quantas unidades deseja comprar ? "))


if produto["estoque"] < add_estoque:
    print("estoque insuficiente")
else:
    produto["estoque"] -= add_estoque
#Para adicionar uma nova informação ao dicionário, você utiliza uma chave:
print(f" Estoque atual: {produto["estoque"]} " )

