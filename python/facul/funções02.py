def entrada_de_dados():
    n = int(input('Digite um número: '))
    return n

def dobro(n):
    r = n * 2
    return r

def imprimir(result):
    print(f'O dobro é {result}')
    return result


# principal

num = entrada_de_dados()
dobro = dobro(num)
imprimir(dobro)