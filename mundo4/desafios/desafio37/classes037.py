from rich import print
from rich.panel import Panel


class Mensagem:
    def __init__(
        self,
        msg: str = "",
        tipo: str = "mensagem",
        icone: str = ":speech_balloon:",
    ):
        self._mensagem = msg
        self._tipo = tipo
        self._icone = icone

    def _criar_painel(self, cor: str):
        titulo = f"{self._icone} {self._tipo.upper()} {self._icone}"
        return Panel(
            self._mensagem,
            title=titulo,
            border_style=cor,
            style=cor,
        )

    def mostrar(self):
        print(self._criar_painel("cyan"))


class Alerta(Mensagem):
    def __init__(self, msg: str = ""):
        super().__init__(msg, tipo="aviso", icone=":warning:")

    def mostrar(self):
        print(self._criar_painel("yellow"))


class Erro(Mensagem):
    def __init__(self, msg: str = ""):
        super().__init__(msg, tipo="erro", icone=":cross_mark:")

    def mostrar(self):
        print(self._criar_painel("red"))
