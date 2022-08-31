def numeros():
    lista = [9,8,7,6,5,4,3,2,1]
    return lista

def imprimir(result):
    for i in result:
        print(f'{i}', end=' ')
    return i

def principal():
    num = numeros()
    imprimir(num)

principal()