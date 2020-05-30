

class Disciplina:
    def __init__(self, nome, semestre):
        self.nome = nome
        self.semestre = semestre
        self.sala = None

    def __str__(self):
        return "Disciplina: "+self.nome+" Semestre: "+self.semestre


lst_disciplina = []


def cadastrar_disciplina():
    disciplina = input("Qual disciplina gostaria de cadastrar? ")
    semestre = input("Qual semestre? ")
    lst_disciplina.append(Disciplina(disciplina, semestre))


def imprime_disciplina():
    for i, v in enumerate(lst_disciplina):
        print(i, v)
