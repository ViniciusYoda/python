class Mae:
    def __init__(self, nome: str):
        self.nome = nome

    def fazer_pudim(self) -> str:
        return f"{self.nome} faz o pudim tradicional da família."

    def fritar_coxinha(self) -> str:
        return f"{self.nome} frita as coxinhas na panela."


class Filha(Mae):
    def fazer_pudim(self) -> str:
        return f"{self.nome} faz pudim de chocolate no forno."

    def fritar_coxinha(self) -> str:
        return f"{self.nome} frita as coxinhas na air fryer."


class Filho(Mae):
    def fazer_pudim(self) -> str:
        return f"{self.nome} faz pudim de leite na panela de pressão."

    def fritar_coxinha(self) -> str:
        return f"{self.nome} frita as coxinhas por imersão no óleo."
