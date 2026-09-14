class Pessoa:

    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        print("olá, ", self.nome )



p1 = Pessoa("André")
p1.apresentar()

p2 = Pessoa("Aninha Patchulinha")
p2.apresentar()

# self é o proprio objeto que chamou o metodo 
#entao se eu criei um objeto chamado p1, é a mesma coisa de dizer
#self.apresentar