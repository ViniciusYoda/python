# Fazer uma função que tem como parâmetro de entrada um número inteiro positivo n e fornece
# como saída o fatorial desse número.

import math

def entrada_de_dados():
    n = int(input('Digite um número: '))
    return n

def mul(n):
    f = math.factorial(n)
    return f

def imprimir(result):
    print(f'A multiplicação é {result}')

num = entrada_de_dados()
mul = mul(num)
imprimir(mul)