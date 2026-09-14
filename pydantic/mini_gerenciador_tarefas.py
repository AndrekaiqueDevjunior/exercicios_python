####mini criador de tarefas ####
################################
class Tarefa:
    def __init__(self, titulo):
        self.titulo = titulo
        self.concluida = False


class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []


    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa) 

gerenciador = GerenciadorTarefas()

titulo = input("Nova Tarefa")

tarefa = Tarefa(titulo)
