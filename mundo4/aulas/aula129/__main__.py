from classes import Analisador


def main() -> None:
    """Mostra exemplos de uso do método sobrecarregado por tipo."""
    analisador = Analisador()

    # O mesmo método escolhe uma implementação conforme o tipo do argumento.
    exemplos = (
        42,                         # int
        "Python",                   # str
        3.14,                       # float
        ["Python", "Java", "C"],   # list
        {"nome": "Ana", "idade": 25},  # dict
        (10, 20),                   # tuple: usa a implementação genérica
    )

    for valor in exemplos:
        print(analisador.analisar(valor))


if __name__ == "__main__":
    main()
