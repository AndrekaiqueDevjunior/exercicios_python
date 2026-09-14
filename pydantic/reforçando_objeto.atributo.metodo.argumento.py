####MINI SISTEMA DE TAREFAS EM PYTHON#### 


class Tarefa:
    def __init__(self, titulo):
        self.titulo = titulo
        self.concluida = False # sempre será falso e nascerá falsa até ser concluida.


    def concluir(self): #essa função meio que obriga a o parametro concluida a ter o booleano Verdadeiro
        self.concluida = True # algoritmo basico de false pra true com a funcao conluir (def)
        # concluida = atributo do objeto

   # def excluir_tarefa(self, excluir):
      #  self.excluir = excluir

    def adicionar_tarefa(self, adicionar):
        self.adicionar = adicionar


class GerenciadorTarefas: ## criando uma classe chamado GerenciadordeTarefas
    def __init__(self): # método construtor
        self.tarefas = []


    def adicionar_tarefa(self, tarefa)#função adicionar tarefa com parametro tarefa 
        self.tarefas.append(tarefa) # parametros que introduz a lista de tarefas com metodo append ( adicionar) e argumento (tarefa)


#o ponto novo é este:

self.tarefas = [] # lista vazia
#leia assim: 

##este objeto gerenciador tarefas possui um atributo chamado tarefas, 
# que começa como uma lista vazia

#depois:
def adicionar_tarefa(self, tarefa):
    self.tarefas.append(tarefa)

    #tarefa = parametro






tarefa.excluir_tarefa("Estudar Python")




tarefa = Tarefa("Estudar Python")



print(tarefa.titulo)

tarefa.concluir() # 

print(tarefa.concluida)

###############

tarefa.titulo
#objeto.atributo

tarefa.concluir()
#objeto.metodo()

tarefa.alterar_titulo("Estudar FastAPI")
#objeto.metodo(argumento)


gerenciador.adicionar_tarefa(tarefa1)

#objeto gerenciador. método(funcao adicionar tarefa).argumento tarefa1

#pegue o objeto gertenciador, adicione o método adicionar tarefa, e inclua no argumento tarefa1

#Pegue o objeto gerenciador → acesse o método adicionar_tarefa → execute esse método passando tarefa1 como argumento.


class Tarefa:
    def __init__(self, titulo):# metodo construtor, que recebe titulo como parametro 
        self.titulo = titulo
        self.concluida = False # parametro que ja nasce como False, para nenhuma tarefa ser criada como  Concluida ou Null 


input_nome_tarefa = input("Digite o nome da tarefa")

tarefa = Tarefa(input_nome_tarefa)

print("Tarefa Criada:")

print(tarefa.titulo)