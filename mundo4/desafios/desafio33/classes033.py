from abc import ABC
from datetime import date


class Pessoa(ABC):
    def __init__(self, nome, nasc):
        self._nome = nome
        self._nascimento = None
        self.nascimento = nasc
    
    @property
    def nascimento(self):
        return self._nascimento
        
    @nascimento.setter
    def nascimento(self, ano):
        if 1900 <= ano <= date.today().year:
            self._nascimento = ano
        else:
            raise ValueError(f"Ano {ano} e invalido")
        
    @property
    def idade(self):
        return date.today().year - self._nascimento
        
    @idade.setter
    def idade(self, valor):
        raise PermissionError("Voce nao pode alterar a idade, mude o ano nascimento")

    
class Aluno(Pessoa):
    
    cursos_oficiais = ["ADM", "ADS", "ENG", "CONT"]
    
    def __ini__(self, nome: str, nasc: int, curso:str):
        super().__init__(nome, nasc)
        self._curso = None
        self.curso = curso
        
    @property
    def curso(self):
        return self._curso
        
    @curso.setter
    def curso(self, curso):
        if curso in Aluno.cursos_oficiais:
            self._curso = curso
        else:
            self._curso = None
            raise ValueError("O curso nao esta na gradee oficial")
    
    def add_curso(self, curso):
        curso = curso.strip().upper()
        
        if 3 <= len(curso) <=5:
            Aluno.cursos_oficiais.append(curso)
        else:
            raise ValueError(f"Nome {curso} esta fora do padrao")