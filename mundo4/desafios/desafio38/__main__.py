from classes038 import Carrinho, Produto


def main():
    carrinho = Carrinho()

    carrinho.adicionar(Produto("Teclado", 149.90))
    carrinho.adicionar(Produto("Mouse", 79.90))
    carrinho.adicionar(Produto("Monitor", 1_299.99))

    print("CARRINHO")
    print(carrinho)

    removido = carrinho.remover("Mouse")
    print(f"\nProduto removido: {removido}")
    print(f"Quantidade restante: {carrinho.quantidade}")
    print(f"\n{carrinho}")


if __name__ == "__main__":
    main()
