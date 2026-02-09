from rich import print
from rich import inspect

class Funcionario:
    
    empresa = "Tech Solutions"
    
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        
    def apresentacao(self) -> str:
        return f"Olá, meu nome é {self.nome}, trabalho no setor de {self.setor} como {self.cargo} da empresa {Funcionario.empresa}."
        
c1 = Funcionario("João", "TI", "Analista de Sistemas")  
#inspect(c1)
print(c1.apresentacao())