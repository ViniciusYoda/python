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

def resumo(preco, taxa_aumento, taxa_reducao):
    """Exibe um resumo com várias informações sobre o preço."""
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxa_aumento}% de aumento: \t{aumentar(preco, taxa_aumento, True)}')
    print(f'{taxa_reducao}% de redução: \t{diminuir(preco, taxa_reducao, True)}')
    print('-' * 30)