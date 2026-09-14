vendas = [
    {"cliente":"Ana","valor":120, "pago": True},
    {"cliente":"Carlos","valor":80, "pago": False},
    {"cliente":"Marcos","valor":250, "pago": True},
    {"cliente":"Julia","valor":60, "pago": False},
    {"cliente":"Felipe","valor":180, "pago": True}
]

total_recebido = 0
quantidade_pagas = 0
for venda in vendas: # “Para cada venda, 
    if venda["pago"] == True: #$ ela está paga? Se estiver,

        total_recebido += venda["valor"]


        quantidade_pagas =  quantidade_pagas + 1 # aumenta meu contador em 1.”


print("total_recebido: ", total_recebido)

print("quantidade_pagas: ", quantidade_pagas)

#“Para cada venda, ela está paga? Se estiver, aumenta meu contador em 1.”

#len(vendas)
# ---> conta TODOS os itens da lista

###contador dentro do if
## conta SOMENTE os itens que obedecem a condição