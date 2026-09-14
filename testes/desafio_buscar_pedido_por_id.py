pedidos = [
    {"id": 1, "cliente": "Ana", "valor": 120, "status": "pago"},
    {"id": 2, "cliente": "Carlos", "valor": 80, "status": "pendente"},
    {"id": 3, "cliente": "Marcos", "valor": 250, "status": "pago"},
]

def buscar_pedido(pedidos, pedido_id):
#o nome do parâmetro precisa representar aquilo que ele recebe.
# se eu criei uma lista chamada " PEDIDOS", 
# a funcao vai receber esse parametro
# com o mesmo nome
    for pedido in pedidos:
        if pedido["id"] == pedido_id:
            return pedido
    return None
