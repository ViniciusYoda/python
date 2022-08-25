def numeros():
    lista = [5, 4, 3, 2, 1]
    return lista

def verificar(lista):
    num = int(input('Digite o numero: '))
    if num in lista:
        print(f'O número {num} está na lista')
    else:
        print(f'O número {num} não está na lista')

def imprimir(result):
    print(result)

def principal():
    num = numeros()
    verificacao = verificar(num)
    imprimir(verificacao)

principal()