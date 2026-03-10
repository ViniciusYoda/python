from rich import print

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual = 1
        
        print(f":open_book: [blue]Voce acabou de abrir o livro {self.titulo} que tem {self.total_paginas} paginas no total. Voce agora esta na pagina {self.pagina_atual}[/blue]")
        
    def avancar_paginas(self, qtd=1):
        cont = 0
        for pg in range(qtd):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                cont += 1

        print(f":page_facing_up: Agora você está na página {self.pagina_atual}")

    def fim_do_livro(self) -> bool:
        return self.pagina_atual == self.total_paginas
        
l1 = Livro("Quero ver", 85)
l1.avancar_paginas(654)