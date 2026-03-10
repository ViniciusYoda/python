from rich.panel import Panel

class Churrasco:
    consumo_padrao:float = 0.400
    preco_kg:float = 82.40
    
    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.participantes = quant
        
        
    def __str__(self):
        return f"Esse é {self.titulo} com {self.participantes} pessoas participando"
    
    def calcular_qtd_carne(self) -> float:
        return self.participantes * Churrasco.consumo_padrao
    
    def calcular_custo_total(self) -> float:
        return self.calcular_qtd_carne() * self.__class__.preco_kg
    
    def calcular_custo_individual(self) -> float:
        return self.calcular_custo_total() / self.participantes
    
    def analisar(self):
        conteudo = f"Analisando [green]{self.titulo}[/] com [blue]{self.participantes}convidados[/]"
        conteudo+= f"nCada participanete comerá {Churrasco.consumo_padrao}Kg e cada Kg Custa R${Churrasco.preco_kg:,.2f}"
        panel = Panel(conteudo, title=self.titulo)