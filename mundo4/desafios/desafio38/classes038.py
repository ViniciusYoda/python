from numbers import Real


def formata_dinheiro(valor: float):
    valor_formatado = f"{valor:,.2f}"
    valor_formatado = valor_formatado.replace(",", "_").replace(".", ",")
    return f"R$ {valor_formatado.replace('_', '.')}"


class Produto:
    def __init__(self, nome: str, preco: float = 0):
        nome = nome.strip()

        if not nome:
            raise ValueError("O produto deve ter um nome")

        self.nome = nome
        self._preco = 0.0
        self.preco = preco

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor: float):
        if isinstance(valor, bool) or not isinstance(valor, Real):
            raise TypeError("O preco deve ser numerico")

        if valor < 0:
            raise ValueError("O preco nao pode ser negativo")

        self._preco = float(valor)

    def __str__(self):
        return f"{self.nome} ({formata_dinheiro(self.preco)})"


class Carrinho:
    def __init__(self, produtos: list | None = None):
        self.produtos = []

        if produtos is not None:
            for produto in produtos:
                self.adicionar(produto)

    def adicionar(self, produto: Produto):
        if not isinstance(produto, Produto):
            raise TypeError("O carrinho aceita apenas objetos da classe Produto")

        self.produtos.append(produto)

    def remover(self, nome: str):
        nome = nome.strip().lower()

        for produto in self.produtos:
            if produto.nome.lower() == nome:
                self.produtos.remove(produto)
                return produto

        raise ValueError(f"O produto '{nome}' nao esta no carrinho")

    @property
    def total(self):
        return sum(produto.preco for produto in self.produtos)

    @property
    def quantidade(self):
        return len(self.produtos)

    def __len__(self):
        return self.quantidade

    def __str__(self):
        if not self.produtos:
            return "Carrinho vazio"

        itens = [f"{indice}. {produto}" for indice, produto in enumerate(self.produtos, 1)]
        itens.append(f"Total: {formata_dinheiro(self.total)}")
        return "\n".join(itens)
