class Caneta:
    def __init__(self, cor = "azul"):
        escolha = ""
        match cor.lower().strip():
            case "azul":
                escolha = "[azul]"
            case "preta":
                escolha = "preta"
            case "vermelha":
                escolha = "vermelha"
            case _:
                escolha = "white"
        self.cor = escolha
        self.tampada = True


    def escrever(self, texto):
        if self.tampada:
            print("A caneta está tampada. Não é possível escrever.")
        else:
            print(f"{self.cor} {texto} [/]")
        
    def quebrar_linha(self):
        print("A caneta quebrou a linha.")
        
    def tampar(self):
        self.tampada = True
        print("A caneta foi tampada.")
        
    def destampar(self):
        self.tampada = False
        print("A caneta foi destampada.")
        
    

c1 = Caneta("azul")
c1.destampar()
c1.escrever("Olá, mundo!")
