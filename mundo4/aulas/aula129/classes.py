"""Classes usadas na demonstração de despacho por tipo."""

from functools import singledispatchmethod
from typing import Any


class Analisador:
    """Descreve valores de acordo com o seu tipo."""

    @singledispatchmethod
    def analisar(self, valor: Any) -> str:
        """Retorna uma descrição para ``valor``."""
        return f"Não foi possível analisar o valor {valor!r}."

    @analisar.register
    def _(self, valor: int) -> str:
        return f"{valor} é um número inteiro."

    @analisar.register
    def _(self, valor: str) -> str:
        return f"{valor!r} é uma cadeia de caracteres."

    @analisar.register
    def _(self, valor: float) -> str:
        return f"{valor} é um número de ponto flutuante."

    @analisar.register
    def _(self, valor: list) -> str:
        return f"{valor!r} é uma lista com {len(valor)} elemento(s)."

    @analisar.register
    def _(self, valor: dict) -> str:
        return f"{valor!r} é um dicionário com {len(valor)} item(ns)."
