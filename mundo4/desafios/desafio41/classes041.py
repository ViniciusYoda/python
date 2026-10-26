import sqlite3
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path


CAMINHO_BANCO = Path(__file__).resolve().parent / "meubanco.db"


class DataNascimentoInvalida(ValueError):
    pass


def converter_data(valor):
    if valor is None or not str(valor).strip():
        raise DataNascimentoInvalida("data de nascimento vazia")

    texto = str(valor).strip()

    if texto.isdigit() and len(texto) == 4:
        raise DataNascimentoInvalida(
            "data incompleta: informe dia, mes e ano"
        )

    formatos = ("%Y-%m-%d", "%d/%m/%Y")

    for formato in formatos:
        try:
            nascimento = datetime.strptime(texto, formato).date()
            break
        except ValueError:
            nascimento = None

    if nascimento is None:
        raise DataNascimentoInvalida(
            "data invalida: use o formato DD/MM/AAAA"
        )

    if nascimento > date.today():
        raise DataNascimentoInvalida("a data de nascimento nao pode ser futura")

    return nascimento


def calcular_idade(nascimento: date, hoje: date | None = None):
    hoje = hoje or date.today()
    ainda_nao_fez_aniversario = (hoje.month, hoje.day) < (
        nascimento.month,
        nascimento.day,
    )
    return hoje.year - nascimento.year - ainda_nao_fez_aniversario


@dataclass
class Pessoa:
    id: int
    nome: str
    nascimento_original: object
    nascimento: date | None = field(init=False, default=None)
    erro_data: str | None = field(init=False, default=None)

    def __post_init__(self):
        try:
            self.nascimento = converter_data(self.nascimento_original)
        except DataNascimentoInvalida as erro:
            self.erro_data = str(erro)

    @property
    def nascimento_formatado(self):
        if self.nascimento is None:
            return f"Nao informado ({self.erro_data})"
        return self.nascimento.strftime("%d/%m/%Y")

    @property
    def idade(self):
        if self.nascimento is None:
            return None
        return calcular_idade(self.nascimento)


def buscar_pessoas(busca: str = ""):
    if not CAMINHO_BANCO.is_file():
        raise FileNotFoundError(f"Banco de dados nao encontrado: {CAMINHO_BANCO}")

    with sqlite3.connect(CAMINHO_BANCO) as banco:
        banco.row_factory = sqlite3.Row
        registros = banco.execute(
            """
            SELECT id, nome, nascimento
            FROM amigos
            WHERE nome LIKE ?
            ORDER BY nome COLLATE NOCASE
            """,
            (f"%{busca.strip()}%",),
        ).fetchall()

    return [
        Pessoa(
            id=registro["id"],
            nome=registro["nome"],
            nascimento_original=registro["nascimento"],
        )
        for registro in registros
    ]
