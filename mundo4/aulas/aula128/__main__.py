from classes import Filha, Filho, Mae


def cozinhar(pessoas: list[Mae]) -> None:
    """Executa os mesmos métodos com resultados diferentes."""
    for pessoa in pessoas:
        print(pessoa.fazer_pudim())
        print(pessoa.fritar_coxinha())
        print()


def main() -> None:
    familia: list[Mae] = [
        Mae("Maria"),
        Filha("Ana"),
        Filho("Pedro"),
    ]
    cozinhar(familia)


if __name__ == "__main__":
    main()
