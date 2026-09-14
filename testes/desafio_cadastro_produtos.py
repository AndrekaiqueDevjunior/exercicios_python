produtos = [
    {"nome": "Teclado", "preco": 100},
    {"nome": "Mouse", "preco": 50},
    {"nome": "Monitor", "preco": 800}
]    #CHAVE              #VALOR



indice =  input("Digite o nome do produto: ") #nome do produto
novo_preco =  int(input("Digite o novo preco: "))



novo_produto = {
    "nome": indice,
    "preco": novo_preco

}

produtos.append(novo_produto)

#produtos[indice]["preco"] = novo_preco
##é alteração.


    

    #indice → produtos[indice] → chave
    #print(f"PRODUTO:  {produtos[indice]['nome']}   ")
    #print(f"PRECO {produtos[indice]['preco']}   ")
    #print(f"PRECO NOVO: {novo_preco} ")
    #print(f"Novo dicionario:  {novo_produto}")
for produto in produtos:
    print(f"Dicionário: {produto['nome']} - {produto['preco']} ")
    #print(f"Produtos {produtos}")
        #print(f"PRECO {produtos[indice][novo_preco]}   ")


#1. Buscar um específico:

#produtos[indice]["nome"]

#2. Percorrer todos:

#for produto in produtos:
 #   produto["nome"]


#if indice == 2:
 #   print(f"PRODUTO:  {produtos[indice]["nome"]}   ")
  #  print(f"NOME:  {produtos[indice]["preco"]}   ")
   
#if indice == 3:
 #   print(f"PRODUTO:  {produtos[indice]["nome"]}   ")
  #  print(f"NOME:  {produtos[indice]["preco"]}   ")
    