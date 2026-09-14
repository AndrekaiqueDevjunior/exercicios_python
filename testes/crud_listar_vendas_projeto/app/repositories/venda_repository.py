###Repository é uma camada de acesso aos dados.###
###Ele encapsula operações como:###

#buscar()
#buscar_por_cliente()
#salvar()
#atualizar()
#deletar()

#Enquanto o Service fica responsável por coisas como:

#"Pode realizar essa operação?"
#"Qual regra deve ser aplicada?"
#"Qual cálculo preciso fazer?"
#"Qual fluxo devo executar?"

#service = VendaService(repository)

#VendaService -> cria um objeto -> service


#class VendaService:
 
  #  def __init__(self, repository): # metodo construtor que recebe como parametro
            # objeto, e repository
      #  self.repository = repository

# repository
# argumento passado para VendaService
# __init__(self, repository)
# self.repository = repository

vendas = [
    {"cliente": "Ana", "valor": 120},
    {"cliente": "Carlos", "valor": 150},
    {"cliente": "Marcos", "valor": 250}
]