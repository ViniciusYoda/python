def numeros():
    lista = [5, 4, 3, 2, 1]
    return lista

def maior(lista):
    menor = lista[0]
    if lista[1] < menor:
        menor = lista[1]
    elif lista[2] < menor:
        menor = lista[2]
    elif lista[3] < menor:
        menor = lista[3]
    elif lista[4] < menor:
        menor = lista[4]
    return menor

def imprimir(result):
    print(result)

def principal():
    num = numeros()
    resultado = maior(num)
    imprimir(resultado)

principal()
