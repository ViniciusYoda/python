"""Exemplo de polimorfismo por duck typing."""


class Porta:
    def abrir(self) -> None:
        print("Girando a maçaneta para abrir a porta.")


class Empresa:
    def abrir(self) -> None:
        print("Criando um CNPJ para abrir a empresa.")


class Ovo:
    def abrir(self) -> None:
        print("Quebrando a casca para abrir o ovo.")


class Livro:
    """Objeto sem o método abrir, usado para demonstrar o erro."""

    def __str__(self) -> str:
        return "livro"


def tentar_abrir(objeto: object) -> None:
    """Tenta abrir qualquer objeto que possua um método abrir()."""
    try:
        abrir = getattr(objeto, "abrir")
    except AttributeError:
        print(f"Não sei como abrir o objeto {objeto!s}.")
        return

    abrir()
