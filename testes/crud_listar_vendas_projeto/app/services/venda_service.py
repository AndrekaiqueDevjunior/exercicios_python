#$###Agora vamos para o próximo passo da arquitetura:
#tirar a regra de negócio do Router e colocar no Service.
from app.data.vendas import vendas
from app.repositories.venda_repository import vendas

def listar_vendas():
    return vendas

#O Service não deve importar o Router.

def buscar_venda(cliente_procurado):
    for venda in vendas:
        if venda["cliente"] == cliente_procurado:
            return venda

    return None





def adicionar_venda(cliente,valor):

    nova_vendas = {
        "cliente": cliente,
        "valor": valor
    }


    vendas.append(nova_vendas)

   # resultado = adicionar_venda(vendas,"André Kaique", 250)

    return vendas


def atualizar_venda(cliente_procurado, novo_valor):
    for venda in vendas:##Percorrer vendas

        if venda["cliente"] == cliente_procurado: # #Procurar pelo cliente
            #venda vai representar um elemento da lista por vez.

            venda["valor"] = novo_valor # #Alterar o valor


            return venda # #Retornar a venda alterada
        #Porque venda é o dicionário específico que encontramos.

    return None # #Se não encontrar, retornar None



def deletar_venda(vendas, cliente_procurado):
#Perfeito. A assinatura está correta.

    for venda in vendas:
        if venda["cliente"] == cliente_procurado:
            vendas.remove(venda)## remover UMA venda

            return {
                "Mensagem": "venda removida com sucesso",
                "venda": venda # aponta diretamente para venda
            }

    return None


    
 #Ela deve:

#Percorrer vendas
#Procurar pelo cliente
#Alterar o valor
#Retornar a venda alterada
#Se não encontrar, retornar None
#Lista = []
#dicionario = {chave:"",valor:""}