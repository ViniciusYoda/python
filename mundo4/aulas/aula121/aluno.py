from .pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self):
        super().__init__(nome="João", idade=20)
        self.curso = "Engenharia"
        self.turma = "2024"
        
    def fazer_matricula(self):
        print(f"{self.nome} matriculado no curso de {self.curso}, turma {self.turma}.")
        