##HERANÇA EM PYTHON##



class Pessoa:
    def __init__(self, nome):
        self.nome = nome

### criamos uma classe base 


###Depois:

class Tecnico(Pessoa):

#aqui estamos dizendo:
## Tecnico é uma especialização de Pessoa, ou Herda de Pessoa



###quando fazemos:

tecnico = Tecnico("André") # aqui estamos criando um objeto da classe Tecnico que recebe um parametro nome que eh uma instancia da classe Pessoa

#python procura um:

__init__() # o metodo construtor da classe Tecnico que recebe um parametro nome que eh uma instancia da classe Pessoa 

#em Tecnico  

#nao encontra

## entao procura na classe pai:

Pessoa 

##encontra:

def __init__(self, nome): ## aqui estamos criando um metodo construtor da classe Pessoa que recebe um parametro nome
  #e executa


  