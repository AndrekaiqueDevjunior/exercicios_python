class Lampada:

    def __init__(self):
        self.ligada = False #

    def ligar_lampada(self):
        self.ligada = True #

    def desligar_lampada(self):
        self.ligada = False #

    def status(self):
        if self.ligada:
            return "ligada"
        else:
            return "desligada"


lamp1 = Lampada() #false

print(lamp1.status()) # desligada

lamp1.ligar_lampada() # TRUE ligada lampada
print(lamp1.status()) ## ligar lampada

lamp1.desligar_lampada() # Desligada
print(lamp1.status()) # desligada 
