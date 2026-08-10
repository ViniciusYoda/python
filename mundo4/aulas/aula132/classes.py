"""Polimorfismo: cada objeto possui sua própria forma de dobrar."""


class Lista:
    def __init__(self, valores: list | None = None) -> None:
        self.valores = list(valores) if valores is not None else []

    def dobrar(self) -> None:
        self.valores = [valor * 2 for valor in self.valores]
        print(f"Valores da lista dobrados: {self.valores}")


class Papel:
    def __init__(self) -> None:
        self.dobrado = False

    def dobrar(self) -> None:
        self.dobrado = True
        print("O papel foi dobrado.")


class Casa:
    def __init__(self, comodos: int = 2) -> None:
        self.comodos = comodos

    def dobrar(self) -> None:
        self.comodos *= 2
        print(f"Quantidade de cômodos dobrada: {self.comodos}")


class Texto:
    def __init__(self, texto: str = "") -> None:
        self.texto = texto

    def dobrar(self) -> None:
        self.texto *= 2
        print(f"Texto duplicado: {self.texto}")


class Numero:
    def __init__(self, valor: int | float = 0) -> None:
        self.valor = valor

    def dobrar(self) -> None:
        self.valor *= 2
        print(f"Número dobrado: {self.valor}")


def dobrar_objeto(objeto: object) -> None:
    """Chama a implementação de dobrar() correspondente ao objeto."""
    dobrar = getattr(objeto, "dobrar", None)
    if not callable(dobrar):
        raise TypeError(f"{type(objeto).__name__} não possui o método dobrar().")
    dobrar()
