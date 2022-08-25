def numeros():
    lista = [5, 4, 3, 2, 1]
    return lista

def produto(lista):
    soma = 1
    for i in lista:
        i *= 4
        soma += 1
    return soma

def imprimir(result):
    print(result)

def principal():
    num = numeros()
    resultado = produto(num)
    imprimir(resultado)

principal()
    