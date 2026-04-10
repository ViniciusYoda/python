from .pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self):
        super().__init__(nome="Dr. Silva", idade=45)
        self.especialidade = "Matemática"
        self.nivel = "Doutor"
        
    def dar_aula(self):
        print(f"{self.nome} está dando aula de {self.especialidade}.")