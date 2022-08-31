def entrada_de_dados():
    n = int(input('Digite um número: '))
    return n

def menor(n1, n2, n3):
    menor = n1
    if n2 < menor:
        menor = n2
    elif n3 < menor:
        menor = n3
    return menor

def imprimir(result):
    print(f'O menor número é  {result}')
    return result

#principal

n1 = entrada_de_dados()
n2 = entrada_de_dados()
n3 = entrada_de_dados()
menor = menor(n1, n2, n3)
imprimir(menor)