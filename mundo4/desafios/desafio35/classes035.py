from abc import ABC, abstractmethod


class Arquivo(ABC):
    formatos_suportados = ("pdf", "doc")

    def __init__(self, nome: str, ext: str, tam: int = 0):
        self.nome = nome
        self._extensao = None
        self.extensao = ext
        self.tamanho = tam

    @abstractmethod
    def abrir(self):
        pass

    @property
    def extensao(self):
        return self._extensao

    @extensao.setter
    def extensao(self, ext: str):
        ext = ext.lower().strip()

        if ext not in self.formatos_suportados:
            raise AttributeError("O arquivo esta em um formato nao suportado")

        self._extensao = ext


class PDF(Arquivo):
    def __init__(self, nome: str, tam: int = 0):
        super().__init__(nome, "pdf", tam)

    def abrir(self):
        return f"Abrindo {self.nome}.{self.extensao} no leitor de PDF"


class DOC(Arquivo):
    def __init__(self, nome: str, tam: int = 0):
        super().__init__(nome, "doc", tam)

    def abrir(self):
        return f"Abrindo {self.nome}.{self.extensao} no editor de documentos"
