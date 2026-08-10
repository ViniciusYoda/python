from classes import Carteira


def main() -> None:
    """Demonstra como consultar e alterar o saldo de forma segura."""
    carteira = Carteira(100)
    print(carteira)

    carteira.depositar(50)
    print(f"Depois do depósito: {carteira}")

    carteira.sacar(30)
    print(f"Depois do saque: {carteira}")

    # __iadd__: equivale a carteira.depositar(80).
    carteira += 80
    print(f"Depois de carteira += 80: {carteira}")

    # __isub__: equivale a carteira.sacar(20).
    carteira -= 20
    print(f"Depois de carteira -= 20: {carteira}")

    # __eq__: compara o saldo de duas carteiras usando ==.
    outra_carteira = Carteira(180)
    print(f"As carteiras são iguais? {carteira == outra_carteira}")

    outra_carteira.sacar(10)
    print(f"Após o saque, são iguais? {carteira == outra_carteira}")

    # A propriedade pode ser consultada normalmente.
    print(f"Consulta direta do saldo: R$ {carteira.saldo:.2f}")

    # Mas não pode ser alterada sem passar pelos métodos da classe.
    try:
        carteira.saldo = 1_000
    except AttributeError as erro:
        print(f"Alteração bloqueada: {erro}")

    try:
        carteira.sacar(500)
    except ValueError as erro:
        print(f"Saque bloqueado: {erro}")


if __name__ == "__main__":
    main()
