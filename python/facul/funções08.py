import math

def entrada_de_dados():
    n = int(input('Digite um número: '))
    return n

def calcularEquacao2(a, b, c):
    delta = b ** 2 - 4 * a * c
    return delta

def raiz(a, b, c, delta):
    x = - (-b) + math.sqrt(delta) / 2 * a
    y = - (-b) - math.sqrt(delta) / 2 * 4

def imprimir(result):
    print(f'A raiz maior do delta é {result}')

a = entrada_de_dados()
b = entrada_de_dados()
c = entrada_de_dados()
equacao = calcularEquacao2(a,b,c)
raiz = raiz(equacao)
imprimir(raiz)