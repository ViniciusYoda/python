from .pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.cargo = "Secretário"
        self.setor = "Administração"
        
    def bater_ponto(self):
        print(f"{self.nome} bateu o ponto no setor de {self.setor}.")