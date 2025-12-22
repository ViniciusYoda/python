def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    print(f'Contagem de {i} até {f} de {p} em {p}')
    c = i
    while c <=f:
        print(f'{c}', end=' ')
        c += p
    print('Fim')

help(contador)
contador(0, 100, 10)

def somar(a, b, c=0):
    """
    -> Faz a soma de três números.
    :param a: primeiro número
    :param b: segundo número
    :param c: terceiro número
    :return: sem retorno
    """
    s = a + b + c
    print(f'A soma de {a}, {b} e {c} é igual a {s}')

somar(3, 5, 7)

def teste(b):
    """
    -> Teste de função.
    :param b: valor a ser testado
    :return: sem retorno
    """
    global a  # Variável global
    a = 8  # Variável local
    print(f'A dentro vale {a}')
    b += 4  # Variável local
    print(f'A fora vale {a}')
    print(f'B dentro vale {b}')
    return b

teste(6)
print(f'A fora vale {a}')

def s(a=0, b=0, c=0):
    s = a + b + c
    return s

s(3, 2, 5)
s(3, 2)
