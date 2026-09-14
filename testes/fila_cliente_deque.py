from collections import deque

filaClientes = deque(["Ciclano","João"])
print(f'Tamanho : {len(filaClientes)}, Fila: {filaClientes}')

filaClientes.extend(['Beltrano','José'])
print(f'Tamanho : {len(filaClientes)}, Fila: {filaClientes}')

filaClientes.append('Fulano')
print(f'Tamanho : {len(filaClientes)}, Fila: {filaClientes}')

while filaClientes:
    print("Atendendo:", filaClientes.popleft())


#metodo = append é igual á feito para adicionar elementos no final
# metodo = extend é igual á  adiciona os elementos de uma lista ou iteravel ao final da lista
# metodo len = conta a quantidade de elementos 
