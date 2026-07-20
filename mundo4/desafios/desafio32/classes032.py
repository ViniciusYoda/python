from hashlib import sha256

class ContaBancaria:
    """"
    Cria uma conta banária e permite fazer saques e depósitos
    
    """
    def __init__(self, id: int, nome:str = None, saldo:float = 0, chave:str = None):
        self._id = id
        self._titular = nome
        self._saldo = saldo
        self.__hash = sha256(chave.encode()).hexdigest()
        
    def pede_senha(self):
        
        from pwinput import pwinput
        while True:
            senha = str(pwinput("Senha: ")).strip()
            
            if len(senha) >= 6:
                break
        return senha
    
    def validar_senha(self, chave) -> bool:
        usuario = sha256(chave.encode()).hexdigest()
        if usuario == self.__hash:
            return True
        else:
            return False
            
        
    def __str__(self):
        return f"A conta {self.id} de {self._titular} tem R${self._saldo:,.2f} de saldo."
    
    def depositar(self, valor):
        valor = abs(valor)
        self._saldo+=valor
        print(f"Depósito de R${valor:,.2f} na conta {self.id} de {self._titular}. Saldo atual: R${self._saldo:,.2f}")
        
    def sacar(self, valor: float, chave:str = None):
        valor = abs(valor)
        if chave is None:
            chave = self.pede_senha()
            
        if self.validar_senha(chave):
            if valor > self._saldo:
                print(f"Saque negado de {self._saldo} na conta {self._id}")
            else:
                self._saldo-=valor
                print(f"Saque de R${valor:,.2f} na conta {self.id} de {self._titular}. Saldo atual: R${self._saldo:,.2f}")
                
    @property
    def nome(self):
        return self._titular
    
    @nome.setter
    def nome(self, novonome: str = None):
        chave = self.pede_senha()
        
        if self.validar_senha(chave):
            if len(novonome) >= 5:
                self._titular = novonome
            else:
                print("Nao posso alterar o nome")