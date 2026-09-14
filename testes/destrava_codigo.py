class Carro:
    def __init__(self, modelo):
        self.modelo = modelo

    def trocar_modelo(self, novo_modelo):
        self.modelo = novo_modelo


carro = Carro("C3")
#um objeto carro, e nós alteramos o atributo dele.
carro.trocar_modelo("Civic")

print(carro.modelo)

# criamos um objeto celular que recebe a classe Celular com um valor string escrito SAMSUNG

#Aqui nós criamos um objeto chamado celular a partir da classe Celular e passamos "Samsung" para o parâmetro marca.