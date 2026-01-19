class ContaBancaria:
    """"
    Cria uma conta banária e permite fazer saques e depósitos
    
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.nome = nome
        self.saldo = saldo
        
    def __str__(self):
        return f"A conta {self.id} de {self.nome} tem R${self.saldo:,.2f} de saldo."
    
    def depositar(self, valor):
        self.saldo+=valor
        
    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saque negado de {self.saldo} na conta {self.id}")
        else:
            self.saldo-=valor
    
c1 = ContaBancaria(123, "Gustavo", 3000)
c1.depositar(500)
c1.sacar(27000)
print(c1)