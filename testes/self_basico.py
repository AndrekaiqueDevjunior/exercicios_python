class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Meu nome é {self.nome} e tenho {self.idade} anos.")

pessoa1 = Pessoa("André", 28)
pessoa2 = Pessoa("Ana Maria", 24)
pessoa1.apresentar()
pessoa2.apresentar()