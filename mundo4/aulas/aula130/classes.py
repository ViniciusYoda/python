"""Exemplo de encapsulamento usando propriedades."""


class Carteira:
    """Representa uma carteira cujo saldo só muda por operações válidas."""

    def __init__(self, saldo_inicial: int | float = 0) -> None:
        self.__saldo = self._validar_valor(saldo_inicial)

    def __str__(self) -> str:
        return f"Você tem R$ {self.saldo:,.2f} na carteira."

    def __eq__(self, outra: object) -> bool:
        """Compara duas carteiras pelo saldo."""
        if not isinstance(outra, Carteira):
            return NotImplemented
        return self.saldo == outra.saldo

    def __iadd__(self, valor: int | float) -> "Carteira":
        """Permite depositar usando ``carteira += valor``."""
        self.depositar(valor)
        return self

    def __isub__(self, valor: int | float) -> "Carteira":
        """Permite sacar usando ``carteira -= valor``."""
        self.sacar(valor)
        return self

    @property
    def saldo(self) -> float:
        """Retorna o saldo atual sem permitir alteração direta."""
        return self.__saldo

    @saldo.setter
    def saldo(self, valor: int | float) -> None:
        raise AttributeError(
            "O saldo não pode ser alterado diretamente; use depositar() ou sacar()."
        )

    def depositar(self, valor: int | float) -> None:
        """Adiciona um valor positivo à carteira."""
        self.__saldo += self._validar_valor(valor)

    def sacar(self, valor: int | float) -> None:
        """Retira um valor da carteira se houver saldo suficiente."""
        valor_validado = self._validar_valor(valor)
        if valor_validado > self.__saldo:
            raise ValueError("Saldo insuficiente.")
        self.__saldo -= valor_validado

    @staticmethod
    def _validar_valor(valor: int | float) -> float:
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError("O valor deve ser um número.")
        if valor < 0:
            raise ValueError("O valor não pode ser negativo.")
        return float(valor)
