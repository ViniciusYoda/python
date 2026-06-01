class ContaBancaria:
    """"
    Cria uma conta banária e permite fazer saques e depósitos
    
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self._titular = nome
        self._saldo = saldo
        
    def __str__(self):
        return f"A conta {self.id} de {self._titular} tem R${self._saldo:,.2f} de saldo."
    
    def depositar(self, valor):
        valor = abs(valor)
        self._saldo+=valor
        print(f"Depósito de R${valor:,.2f} na conta {self.id} de {self._titular}. Saldo atual: R${self._saldo:,.2f}")
        
    def sacar(self, valor):
        valor = abs(valor)
        if valor > self._saldo:
            print(f"Saque negado de {self._saldo} na conta {self.id}")
        else:
            self._saldo-=valor
            print(f"Saque de R${valor:,.2f} na conta {self.id} de {self._titular}. Saldo atual: R${self._saldo:,.2f}")