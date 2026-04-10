class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def fazer_aniversario(self):
        self.idade += 1
        print(f"Parabéns {self.nome}! Agora você tem {self.idade} anos.")