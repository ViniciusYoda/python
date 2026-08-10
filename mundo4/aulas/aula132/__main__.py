from classes import Casa, Lista, Numero, Papel, Texto, dobrar_objeto


def main() -> None:
    """Demonstra diferentes objetos respondendo ao método dobrar()."""
    objetos = (
        Lista([1, 2, 3]),
        Papel(),
        Casa(3),
        Texto("Python "),
        Numero(10),
    )

    for objeto in objetos:
        dobrar_objeto(objeto)


if __name__ == "__main__":
    main()
