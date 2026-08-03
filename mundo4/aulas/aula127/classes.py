from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, nome: str):
        self.nome = nome

    @abstractmethod
    def emitir_som(self) -> str:
        """Retorna o som característico do animal."""
        raise NotImplementedError

class Pato(Animal):
    def emitir_som(self) -> str:
        return f"{self.nome} está grasnando: Quá-quá!"

class Cachorro(Animal):
    def emitir_som(self) -> str:
        return f"{self.nome} está latindo: Au-au!"
    
class Spitz(Cachorro):
    def emitir_som(self) -> str:
        return f"{self.nome} está latindo: Yip-yip!"

class Pitbull(Cachorro):
    def emitir_som(self) -> str:
        return f"{self.nome} está latindo: Woof-woof!"

class Gato(Animal):
    def emitir_som(self) -> str:
        return f"{self.nome} está miando: Miau!"

class Galinha(Animal):
    def emitir_som(self) -> str:
        return f"{self.nome} está cacarejando: Có-có!"
