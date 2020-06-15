

class Disciplina:
    def __init__(self, nome, semestre):
        self.nome = nome
        self.semestre = semestre
        self.sala = None

    def set_sala_disciplina(self, sala):
        self.sala = sala

    def get_sala(self):
        if self.sala is None:
            return "Sala: não definida!"
        if self.sala is not None:
            return self.sala

    def get_semestre(self):
        return self.semestre

    def get_nome(self):
        return self.nome

    def __str__(self):
        return "Disciplina: "+self.nome+" Semestre: "+self.semestre+" "+str(self.get_sala())



