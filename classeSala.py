class Sala:
    def __init__(self, numero):
        self.numero = numero
        self.andar = self.setAndar(numero)
        self.capacidade = None

    def setAndar(self, numero):
        self.andar = numero[0]
        return self.andar

    def set_capacidade(self, capacidade):
        self.capacidade = capacidade

    def get_sala(self):
        return self.numero

    def set_sala(self, sala):
        self.numero = sala

    def __str__(self):
        return "Sala: "+self.numero+" Andar: "+str(self.andar)+" Capacidade: "+self.capacidade




