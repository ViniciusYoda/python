def moeda(valor, simbolo='R$'):
    """Formata um valor monetário."""
    return f'{simbolo}{valor:.2f}'.replace('.', ',')

def aumentar(preco, taxa, formato=False):
    """Calcula o aumento de um preço em uma determinada taxa percentual."""
    resultado = preco + (preco * taxa / 100)
    return moeda(resultado) if formato else resultado

def diminuir(preco, taxa, formato=False):
    """Calcula a redução de um preço em uma determinada taxa percentual."""
    resultado = preco - (preco * taxa / 100)
    return moeda(resultado) if formato else resultado

def dobro(preco, formato=False):
    """Calcula o dobro de um preço."""
    resultado = preco * 2
    return moeda(resultado) if formato else resultado

def metade(preco, formato=False):
    """Calcula a metade de um preço."""
    resultado = preco / 2
    return moeda(resultado) if formato else resultado