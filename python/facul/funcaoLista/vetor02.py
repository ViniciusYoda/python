def numeros():
    lista = [5, 4, 3, 2, 1]
    return lista

def maior(lista):
    maior = lista[0]
    if lista[1] > maior:
        maior = lista[1]
    elif lista[2] > maior:
        maior = lista[2]
    elif lista[3] > maior:
        maior = lista[3]
    elif lista[4] > maior:
        maior = lista[4]
    return maior

def imprimir(result):
    print(result)

def principal():
    num = numeros()
    resultado = maior(num)
    imprimir(resultado)

principal()

