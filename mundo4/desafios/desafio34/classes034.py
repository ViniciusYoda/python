from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome: str = None, salario:float = 1_621):
        self.nome = nome
        self.__salario = salario
        
    @abstractmethod
    def calcular_bonus(self):
        pass
        
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, valor: float = None):
        if valor is None:
            raise ValueError("Impossivel reajjustar o salario desse jeito")
        else:
            if valor >= self.__salario:
                self.__salario = valor
            else:
                raise ValueError("Voce nao pode reduzir o salario")

class Desenvolvedor(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.10

class Designer(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.08

class Gerente(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.15
