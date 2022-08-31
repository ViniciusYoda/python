def pegar_numero():
    n = int(input('Digite um número inteiro positivo: '))
    return n

def primo(n):
    primo = False
    tot = 0
    for c in range(1, n + 1):
        if n % c == 0:
            tot += 1
    if tot == 2:
        primo = True
        print('O número é primo')
    else:
        print('O número não é primo')
    return primo

def principal():
    n = pegar_numero()
    primo(n)

principal()