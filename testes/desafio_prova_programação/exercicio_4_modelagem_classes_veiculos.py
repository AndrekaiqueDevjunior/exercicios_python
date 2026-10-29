# o que pede o exercício
#4- Em uma fábrica de automóveis são fabricados carros flex (alcool e gasolina), diesel e
#elétricos. Todos os carros fabricados levam em consideração uma série de fatores e cada
#um tem dados a serem armazenados.
#- Os carros flex tem ( número do chassi, número do motor, número de portas, cilindrada,
#custo de produção).
#- Os carros diesel tem ( número do chassi, número do motor, capacidade de carga, volume
#da caçamba, custo de produção).
#- Os carros elétricos tem ( número do chassi, número do motor, potência, duração da
#bateria, custo de produção).
#Todos os carros tem imposto de produção fixado em 20%. Os carros à diesel, por serem
#mais poluentes e utilizados para trabalho, tem um acréscimo de 10%, ficando seu imposto
#em 30%. Os carros elétricos tem um incentivo e seu imposto tem um decréscimo de 10%,
#ficando seu imposto em 10%.
#A fábrica tem sobre todos os automóveis um lucro de 25%.
#Modele as classes necessárias, com seus atributos e uma função para calcular o custo de
#venda de cada veículo. O custo de venda é obtido a partir da conta custo de produção +
#imposto + lucro da fábrica. Tanto o imposto quanto o lucro são calculados a partir do custo
#de produção e não são sobrepostos.


#vamos criar a classe carro que:
# instancia um metodo construtor que recebe  self como o metodo construtor
# parametro da instancia : chassi, motor, custo_producao

class Carro:
    def __init__(self, chassi,motor,custo_producao):
        self.chassi = chassi
        self.motor = motor
        self.custo_producao = custo_producao
        self.imposto = 0.20 # #Todos os carros tem imposto de produção fixado em 20%. Os carros à diesel, por serem

        self.lucro = 0.25 ## #A fábrica tem sobre todos os automóveis um lucro de 25%.

    def calcular_custo_venda(self): # Criamos a funcao calcular_custo de venda que:
        ### cria  o custoo que recebe o parametro self.custo_producao.
        ## criamos  o valor imposto que recebe custo de producao vezes  parametro imposto
        # em seguida o valor_lucro que recebe custo de producao vezes o parametro lucro

        # que retorna  a somatoria de custo + valor do imposto + o valor do lucro

        custo = self.custo_producao
        valor_imposto = custo * self.imposto
        valor_lucro = custo * self.lucro
        return custo + valor_imposto + valor_lucro



class CarroFlex(Carro):
    def __init__(self,chassi,motor,portas,cilindrada,custo_producao):
        super().__init__(chassi,motor,custo_producao)
        self.portas = portas
        self.cilindrada = cilindrada






# criamos a classe filha que herda atributos e métodos da classe clarro
# classe filha que recebe  Carro como parametro (logo estamos falando de herança)
# criado o método construtor que recebe self, chassi, motor, portas,cilindradas,custo_producao
# 
##explicacao rapida por que eu usei o metodo super():
# ele serve pra acessar métodos de uma classe pai, ainda mais que o exercício pede herança
# o metodo super que recebe os parametros chassi, motor e custo de producao

# parametro portas : exclusivo da classe filha
# parametro cilindrada :  exclusivo da classe filha
 
class CarroDiesel(Carro):
    def __init__(self, chassi,motor,capacidade_carga,volume_cacamba, custo_producao):
        super().__init__(chassi, motor,custo_producao)

        self.capacidade_carga = capacidade_carga
        self.volume_cacamba = volume_cacamba
        self.imposto = 0.30

#criado a classe filha carro Eletrico que herdas alguns atributoss da classe PAI CARRO
# iniciado o  método construtror que recebe :
# chassi,motor,potencia,duracao_bateria_custo_producao

#iniciado o metodo super que herda atributos da classe pai, como chassi,motor,custo_producao
#recebemos o parametro: potencia, duracao_bateria e imposto de 10%

class CarroEletrico(Carro):
    def __init__(self, chassi,motor,potencia,duracao_bateria,custo_producao):

        super().__init__(chassi,motor,custo_producao)

        self.potencia = potencia
        self.duracao_bateria = duracao_bateria
        self.imposto = 0.10


#exemplos de utilizacao 

flex = CarroFlex("001", "M01", 4, 1.6, 100000) #
diesel = CarroDiesel("002", "M02", 1000, 500, 100000)
eletrico = CarroEletrico("003", "M03", 150, 400, 100000)

print("Flex:", flex.calcular_custo_venda())
print("Diesel:", diesel.calcular_custo_venda())
print("Elétrico:", eletrico.calcular_custo_venda())