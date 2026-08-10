from classes import Empresa, Livro, Ovo, Porta, tentar_abrir


def main() -> None:
    """Demonstra objetos diferentes respondendo ao mesmo método."""
    objetos = (Porta(), Empresa(), Ovo(), Livro())

    for objeto in objetos:
        tentar_abrir(objeto)


if __name__ == "__main__":
    main()
