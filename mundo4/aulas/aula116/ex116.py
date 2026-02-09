class Gafanhoto:
    def __init__(self):
        self.nome = ""
        self.idade = 0


    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos de idade"

g1 = Gafanhoto()

g1.nome = "Maria"

g1.idade = 18

g1.aniversario()

print(g1.mensagem())