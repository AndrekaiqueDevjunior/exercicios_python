pedidos = [
    {"id": 1, "cliente": "Ana", "valor": 120, "status": "pago"},
    {"id": 2, "cliente": "Carlos", "valor": 80, "status": "pendente"},
    {"id": 3, "cliente": "Marcos", "valor": 250, "status": "pago"},
    {"id": 4, "cliente": "Julia", "valor": 60, "status": "cancelado"},
]


def buscar_produto(produtos, produto_id):
    for pedido in pedidos:
        if pedido["id"] = produto_id: