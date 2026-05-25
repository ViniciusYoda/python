from abc import ABC, abstractmethod
import random

class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []
    
    def atacar(self, alvo, forca = 50):
        if self.vida > 0 and alvo.vida > 0:
            dano = forca + random.randint(0, 10)
            alvo.receber_dano(dano)
            print(f"{self.nome} atacou {alvo.nome} com {dano} de dano.")
        
    
    def receber_dano(self, dano):
        fator = random.randint(1, 10) / 10
        self.vida = self.vida - fator
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nome} recebeu {dano} de dano e agora tem {self.vida} de vida.")
    
    @abstractmethod
    def curar(self):
        pass
    
class Guerreiro(Personagem):
    def __init__(self, nome, vida = 100):
        super().__init__(nome, vida)
        self.golpes = ["Corte", "Investida", "Giro"]
        
    def curar(self):
        fator = random.randint(1, 100) 
        self.vida = self.vida + fator
        if self.vida > 100:
            self.vida = 100
        
class Mago(Personagem):
    def __init__(self, nome, vida = 80):
        super().__init__(nome, vida)
        self.golpes = ["Bola de Fogo", "Raio", "Explosão"]
        
    def curar(self):
        fator = random.randint(1, 80) 
        self.vida = self.vida + fator
        if self.vida > 80:
            self.vida = 80