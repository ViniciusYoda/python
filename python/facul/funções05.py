# Fazer uma função que tem como parâmetro de entrada um número inteiro positivo n e fornece como saída a soma de todos os números inteiros menores ou iguais a n.

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

def imprimir(result):
    print(f'A soma é {result}')

num = entrada_de_dados()
soma = soma(num)
imprimir(soma)
    