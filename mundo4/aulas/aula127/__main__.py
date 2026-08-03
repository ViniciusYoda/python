from classes import Animal, Cachorro, Galinha, Gato, Pato


def apresentar_animais(animais: list[Animal]) -> None:
    """Usa a mesma operação para objetos de diferentes classes."""
    for animal in animais:
        print(animal.emitir_som())


def main() -> None:
    animais: list[Animal] = [
        Pato("Donald"),
        Cachorro("Rex"),
        Gato("Garfield"),
        Galinha("Pintadinha"),
    ]
    apresentar_animais(animais)


if __name__ == "__main__":
    main()

