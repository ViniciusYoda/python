from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()
    
    def add_favorites(self, game):
        self.favoritos.append(game)
        self.favoritos = sorted(self.favoritos, key=str.lower)
        
    def ficha(self):
        conteudo = f"Nome real: [black on white] {self.nome} [/]" 
        conteudo += f"\nJogos favoritos"
        for num, game in enumerate(self.favoritos):
            conteudo += f"\n🎮: [blue]{game}[/]"
        painel = Panel(conteudo, title=f"Jogador {self.nick}")
        print(painel)
            
j1 = Gamer("Vinicius", "VYODA")
j1.add_favorites("Supermario")
j1.add_favorites("Sonic")
j1.add_favorites("zELDA")
j1.ficha()
