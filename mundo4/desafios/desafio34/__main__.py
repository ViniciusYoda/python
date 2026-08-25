from classes034 import Desenvolvedor, Designer, Gerente


def main():
    funcionarios = [
        Desenvolvedor("Ana", 5_000),
        Designer("Bruno", 5_000),
        Gerente("Carla", 5_000),
    ]

    for funcionario in funcionarios:
        print(
            f"{funcionario.__class__.__name__}: "
            f"salario = R$ {funcionario.salario:.2f} | "
            f"bonus = R$ {funcionario.calcular_bonus():.2f}"
        )


if __name__ == "__main__":
    main()
