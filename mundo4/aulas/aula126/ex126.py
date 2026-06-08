class Avaliacao:
    def __init__(self, nome, disciplina, nota):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota
        
    @property
    def nota(self):
        return self._nota
    
    @nota.setter
    def nota(self, nota):
        if 0 <= nota <= 10:
            self._nota = nota
        else:
            print("Nota invalida")
        
