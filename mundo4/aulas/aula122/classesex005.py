from abc import ABC, abstractmethod

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def fazer_aniversario(self):
        self.idade += 1
        print(f"Parabéns {self.nome}! Agora você tem {self.idade} anos.")
        
    @abstractmethod
    def estudar(self):
        pass
        
class Aluno(Pessoa):
    def __init__(self):
        super().__init__(nome="João", idade=20)
        self.curso = "Engenharia"
        self.turma = "2024"
        
    def fazer_matricula(self):
        print(f"{self.nome} matriculado no curso de {self.curso}, turma {self.turma}.")
        
    def estudar(self):
        print(f"{self.nome} está estudando para as provas de {self.curso}.")
        
class Professor(Pessoa):
    def __init__(self):
        super().__init__(nome="Dr. Silva", idade=45)
        self.especialidade = "Matemática"
        self.nivel = "Doutor"
        
    def dar_aula(self):
        print(f"{self.nome} está dando aula de {self.especialidade}.")
        
    def estudar(self):
        print(f"{self.nome} está estudando novas metodologias de ensino para {self.especialidade}.")
        
class Funcionario(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.cargo = "Secretário"
        self.setor = "Administração"
        
    def estudar(self):
        return super().estudar()    
        
    def bater_ponto(self):
        print(f"{self.nome} bateu o ponto no setor de {self.setor}.")