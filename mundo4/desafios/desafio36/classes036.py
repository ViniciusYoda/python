from abc import ABC, abstractmethod
from datetime import date, timedelta
from numbers import Real
from uuid import uuid4


class Pagamento(ABC):
    def __init__(self):
        self._valor = None
        self._status = "nao iniciado"

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor: float):
        if isinstance(valor, bool) or not isinstance(valor, Real):
            raise TypeError("O valor do pagamento deve ser numerico")

        if valor <= 0:
            raise ValueError("O valor do pagamento deve ser maior que zero")

        self._valor = float(valor)

    @property
    def status(self):
        return self._status

    @property
    def fvalor(self):
        if self.valor is None:
            return "R$ 0,00"

        valor_formatado = f"{self.valor:,.2f}"
        valor_formatado = valor_formatado.replace(",", "_").replace(".", ",")
        return f"R$ {valor_formatado.replace('_', '.')}"

    def _definir_valor(self, valor: float):
        self.valor = valor

    @abstractmethod
    def pagar(self, valor: float):
        pass


class Boleto(Pagamento):
    def __init__(self, dias_para_vencer: int = 3):
        super().__init__()

        if dias_para_vencer <= 0:
            raise ValueError("O prazo do boleto deve ser maior que zero")

        self.dias_para_vencer = dias_para_vencer
        self.codigo = None
        self.vencimento = None

    def pagar(self, valor: float):
        self._definir_valor(valor)
        self.codigo = uuid4().hex.upper()
        self.vencimento = date.today() + timedelta(days=self.dias_para_vencer)
        self._status = "aguardando pagamento"

        return (
            f"Boleto de {self.fvalor} gerado | "
            f"vencimento: {self.vencimento:%d/%m/%Y} | "
            f"codigo: {self.codigo}"
        )


class Pix(Pagamento):
    def __init__(self, chave_destino: str):
        super().__init__()
        chave_destino = chave_destino.strip()

        if not chave_destino:
            raise ValueError("A chave Pix nao pode ficar vazia")

        self.chave_destino = chave_destino
        self.identificador = None

    def pagar(self, valor: float):
        self._definir_valor(valor)
        self.identificador = uuid4().hex.upper()
        self._status = "confirmado"

        return (
            f"Pix de {self.fvalor} enviado para {self.chave_destino} | "
            f"ID: {self.identificador}"
        )


class CartaoCredito(Pagamento):
    def __init__(self, final_cartao: str, limite: float):
        super().__init__()
        final_cartao = str(final_cartao).strip()

        if len(final_cartao) != 4 or not final_cartao.isdigit():
            raise ValueError("Informe os quatro ultimos digitos do cartao")

        if isinstance(limite, bool) or not isinstance(limite, Real):
            raise TypeError("O limite deve ser numerico")

        if limite <= 0:
            raise ValueError("O limite deve ser maior que zero")

        self.final_cartao = final_cartao
        self.limite = float(limite)
        self.parcelas = None

    def pagar(self, valor: float, parcelas: int = 1):
        self._definir_valor(valor)

        if isinstance(parcelas, bool) or not isinstance(parcelas, int):
            raise TypeError("A quantidade de parcelas deve ser um numero inteiro")

        if not 1 <= parcelas <= 12:
            raise ValueError("O pagamento deve ter entre 1 e 12 parcelas")

        if self.valor > self.limite:
            self._status = "recusado"
            raise ValueError("Pagamento recusado por falta de limite")

        self.parcelas = parcelas
        self.limite -= self.valor
        self._status = "aprovado"
        valor_parcela = self.valor / parcelas

        return (
            f"Pagamento de {self.fvalor} aprovado no cartao final "
            f"{self.final_cartao} | {parcelas}x de {self._formatar(valor_parcela)}"
        )

    @staticmethod
    def _formatar(valor: float):
        valor_formatado = f"{valor:,.2f}"
        valor_formatado = valor_formatado.replace(",", "_").replace(".", ",")
        return f"R$ {valor_formatado.replace('_', '.')}"
