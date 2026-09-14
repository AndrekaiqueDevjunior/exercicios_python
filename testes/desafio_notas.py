notas = [
    7,
    4,
    9,
    5,
    8
]



for indice, notas in enumerate( notas, start=1):
    if notas >= 6:
        print("Aluno", indice, "-", "Nota", notas, "-", "Aprovado")
    if notas < 6:
        print("Aluno", indice, "-", "Nota", notas, "-", "Reprovado")
