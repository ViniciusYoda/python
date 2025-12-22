def aumentar(preco, taxa):
    return preco + (preco * taxa / 100)


def diminuir(preco, taxa):
    return preco - (preco * taxa / 100)


def dobro(preco):
    return preco * 2


def metade(preco):
    return preco / 2


def moeda(preco=0, simbolo='R$'):
    return f'{simbolo}{preco:>8.2f}'.replace('.', ',')