from abc import ABC, abstractmethod

class BebidaQuente(ABC):
    
    def preparar(self):
        print(f"Preparando {self.__class__.__name__}...")
        
        self.ferver_agua()
        self.misturar()
        self.servir()
        
        print(f"{self.__class__.__name__} pronto para ser servido!")
    
    def ferver_agua(self):
        print("Fervendo água...")
    
    @abstractmethod
    def misturar(self):
        pass
    
    @abstractmethod
    def servir(self):
        pass
    
    
class Cafe(BebidaQuente):
    
    def misturar(self):
        print("Misturando café em pó com água fervente...")
    
    def servir(self):
        print("Servindo o café quente...")
        
        
class Cha(BebidaQuente):
    
    def misturar(self):
        print("Colocando o saquinho de chá na água fervente...")
    
    def servir(self):
        print("Servindo o chá quente...")
        
class Leite(BebidaQuente):
    
    def misturar(self):
        print("Aquecendo o leite...")
    
    def servir(self):
        print("Servindo o leite quente...")