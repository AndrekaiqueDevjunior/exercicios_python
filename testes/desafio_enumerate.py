tarefas = [
        "Estudar Python",
        "Treinar FastAPI",
        "Ler",
        "Academia"
]



for indice, tarefa in enumerate (tarefas, start=1):
    if indice <= 2:
        print(indice, "-",  tarefa, "-", "Prioridade Alta" )
    else:     
        print(indice, "-",  tarefa)