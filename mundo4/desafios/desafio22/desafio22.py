from rich import print
from rich.panel import Panel

class ControleRemoto:
    canal_min: int = 1
    canal_max: int = 6
    volume_min: int = 0
    volume_max: int = 10

    def __init__(self, canal: int = canal_min, volume: int = 2):
        self.canal_atual: int = canal
        self.volume_atual: int = volume
        self.ligado: bool = False

    def ligar(self):
        self.ligado = True
        print("TV ligada")

    def desligar(self):
        self.ligado = False
        print("TV desligada")

    def liga_desliga(self):
        self.ligado = not self.ligado
        print("TV ligada" if self.ligado else "TV desligada")

    def mudar_canal(self, canal: int):
        if not self.ligado:
            print("A TV está desligada")
            return
        if self.canal_min <= canal <= self.canal_max:
            self.canal_atual = canal
            print(f"Canal alterado para {canal}")
        else:
            print(f"Canal inválido: {canal}. Intervalo [{self.canal_min}, {self.canal_max}]")

    def canal_seguinte(self):
        if not self.ligado:
            print("A TV está desligada")
            return
        if self.canal_atual < self.canal_max:
            self.canal_atual += 1
        print(f"Canal {self.canal_atual}")

    def canal_anterior(self):
        if not self.ligado:
            print("A TV está desligada")
            return
        if self.canal_atual > self.canal_min:
            self.canal_atual -= 1
        print(f"Canal {self.canal_atual}")

    def aumentar_volume(self):
        if not self.ligado:
            print("A TV está desligada")
            return
        if self.volume_atual < self.volume_max:
            self.volume_atual += 1
        print(f"Volume {self.volume_atual}")

    def diminuir_volume(self):
        if not self.ligado:
            print("A TV está desligada")
            return
        if self.volume_atual > self.volume_min:
            self.volume_atual -= 1
        print(f"Volume {self.volume_atual}")

    def mostrar_tv(self):
        conteudo = ""
        if self.ligado:
            conteudo += f"Canal: [blue]{self.canal_atual}[/]\n"
            conteudo += f"Volume: [red]{self.volume_atual}[/]\n"
            for canal in range(self.canal_min, self.canal_max + 1):
                if canal == self.canal_atual:
                    conteudo += f"[green]> Canal {canal} <[/]\n"
                else:
                    conteudo += f"Canal {canal}\n"
        else:
            conteudo = "TV desligada"

        print(Panel(conteudo.rstrip(), title="TV"))

# exemplo de uso
tv = ControleRemoto()
tv.mostrar_tv()
tv.liga_desliga()
tv.mudar_canal(3)
tv.aumentar_volume()
tv.mostrar_tv()