def entrada_de_dados():
    n = int(input('Digite um número: '))
    return n

def maior(n1, n2):
    maior = n1
    if n2 > maior:
        maior = n2
    else:
        maior = n1
    return maior

def imprimir(result):
    print(f'O maior número é {result}')
    return result

#principal

num1 = entrada_de_dados()
num2 = entrada_de_dados()
maior = maior(num1, num2)
imprimir(f'O maior número entre {num1} e {num2} é {maior}')
    