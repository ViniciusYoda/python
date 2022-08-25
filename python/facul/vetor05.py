def numeros():
    lista = [5, 4, 3, 2, 1]
    return lista

def produtos(lista):
    fat = 1
    for i in lista:
        fat *= i
    return fat

def imprimir(resultado):
    print(resultado)

def principal():
    numero = numeros()
    produto = produtos(numero)
    imprimir(produto)

principal()