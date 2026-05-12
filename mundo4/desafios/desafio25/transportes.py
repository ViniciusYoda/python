from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0
        
    @abstractmethod
    def calcular_frete(self):
        """Calcula o valor do frete com base na distância."""
        pass

class Moto(Transporte):
    fator = 0.50
    
    def calcular_frete(self):
        self.frete = self.distancia * self.fator
        return f"R${self.frete:.2f}"

class Caminhao(Transporte):
    fator = 1.2
    
    def calcular_frete(self):
        if self.distancia < 50:
            return "Erro: Caminhão exige distância mínima de 50km."
        
        self.frete = self.distancia * self.fator
        return f"R${self.frete:.2f}"

class Drone(Transporte):
    fator = 9.50
    
    def calcular_frete(self):
        if self.distancia > 10:
            return "Erro: Drone possui raio máximo de 10km."
        
        self.frete = self.distancia * self.fator
        return f"R${self.frete:.2f}"