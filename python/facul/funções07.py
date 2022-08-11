import math

def entrada_de_dados():
    n = int(input('Digite um número: '))
    return n

def soma(n):
    cont = n
    soma = 0
    while cont != 0:
        soma += cont
        cont -= 1
    return soma

def mul(n):
    f = math.factorial(n)
    return f

def div(n1, n2):
    div = n1 / n2
    return div

def imprimir(result):
    print(f'A multiplicação é {result}')

n1 = entrada_de_dados()
soma = soma(n1)
n2 = entrada_de_dados()
mul = mul(n2)
div = div(mul, soma)
imprimir(div)