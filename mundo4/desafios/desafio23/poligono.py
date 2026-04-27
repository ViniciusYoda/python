from abc import ABC, abstractmethod

class Poligono(ABC):
    
    def __init__(self, lados):
        self.qtd_lados = lados
        
    @abstractmethod
    def perimetoro(self):
        pass
    
    @abstractmethod
    def area(self):
        pass
    
class Quadrado(Poligono):
    
    def __init__(self, lado = 1):
        super().__init__(4)
        self.lado = lado
        
    def perimetoro(self):
        return self.lado * 4
    
    def area(self):
        return self.lado ** 2

class Circulo(Poligono):
    
    def __init__(self, raio):
        super().__init__(0)
        self.raio = raio
        
    def perimetoro(self):
        return 2 * 3.14 * self.raio
    
    def area(self):
        return 3.14 * (self.raio ** 2)
        