vendas = [
    {"cliente": "Ana", "valor": 120},
    {"cliente": "Carlos", "valor": 80}
]

#cliente = ""
#valor = 0 
def adicionar_venda(vendas,cliente,valor):
  
    nova_vendas = { # dicionario
        "cliente": cliente,
        "valor": valor
    }
    #for venda in vendas:


    vendas.append(nova_vendas) # adicionar os novos valores na lista venda
       # porque append() é método de lista.

    return vendas
        
resultado = adicionar_venda(vendas,"andré kaique", 250)
#### variavel resultado recebe adicionar vendas com o parâmetro.
#### (vendas, "andré kaique", 250)
####

####
print(resultado)