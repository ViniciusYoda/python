class Gafanhoto:
    """
        Essa clase cria um Gafanhoto
    """
    def __init__(self, n = "", i = 0):
        self.nome = n
        self.idade = i


    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos de idade"
    
    def __str__(self):
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos de idade"
    
    def __getstate__(self):
        return f"Estado {self.nome}"

g1 = Gafanhoto("Maria", 21)

g1.aniversario()



print(g1.__getstate__())