print('Calculadora simples')

def entrada_de_dados():
    print('Entrada de dados ')
    n = int(input('Digite um número: '))
    return n

def menu():
    print('*- Menu -*')
    print('='*10)
    print('1- Adição ')
    print('2- Subtração ')
    print('3 - Multiplicação ')
    print('4 - Divisão')
    op = int(input('Opção: '))
    return op


def add(n1, n2):
    print('Adição')
    s = n1 + n2
    return s



def sub(n1, n2):
    print('Subtração')
    s = n1 - n2
    return s


def mul(n1, n2):
    print('Multiplicação')
    s = n1 * n2
    return s


def div(n1, n2):
    print('Divisão')
    s = n1 / n2
    return s

def imprimir(result):
    print('Imprimir o resultado')
    print(f'Resultado: {result}')

def controlador(n1, n2, op):
    print('Controlador')
    if op == 1:
        r = add(n1, n2)
    elif op == 2:
        r = sub(n1, n2)
    elif op == 3:
        r = mul(n1, n2)
    elif op == 4:
        r = div(n1, n2)
    else:
        r = 'Opção inválida'
    return r
           
print('*- Principal -*')

while True:
    op = menu()
    n1 = entrada_de_dados()
    n2 = entrada_de_dados()
    result = controlador(n1, n2, op)
    imprimir(result)
    resp = str(input('Quer continuar? [S/N] ')).upper()[0]
    if resp == 'N':
        break



