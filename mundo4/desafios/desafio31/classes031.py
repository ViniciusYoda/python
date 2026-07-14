class Retangulo:
    
    def __init__(self, base = 1, altura = 1):
        self._base = None
        self._altura = None
        self._area = None
        self.base - base
        self.altura = altura
        
    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, valor):
        if not isinstance(valor, float) and not isinstance(valor, int):
            raise TypeError("o VALOR DA BASE DEVE SER UM NUMERO")
        if valor < 0:
            raise ValueError("Valor invalido para a base")
        else:
            self._base = valor
    
    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, valor):
        if not isinstance(valor, float) and not isinstance(valor, int):
            raise TypeError("o VALOR DA BASE DEVE SER UM NUMERO")
        if valor < 0:
            raise ValueError("Valor invalido para a base")
        else:
            self._altura = valor
    
    @property
    def area(self):
        self._area = self._base * self._altura
        return self._area
    
    @area.setter
    def area(self):
        raise PermissionError("Area nao pode ser definida")
    
    @property
    def medidas(self):
        return f"Base = {self.base} \nAltura = {self.altura} \nArea = {self.area}"
    
    @medidas.setter
    def medidas(self, valores:tuple):
        if not isinstance(valores, tuple):
            raise TypeError("Tuplas")
        if len(valores) != 2:
            raise ValueError("Apenas 2 valores")
        if isinstance(valores[0], float) or isinstance(valores[0], int):
            self.base = valores[0]
        else:
            raise TypeError("Num")
        if isinstance(valores[1], float) or isinstance(valores[1], int):
            self.altura = valores[1]
        else:
            raise TypeError("Num")