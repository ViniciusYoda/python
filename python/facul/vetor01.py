def numeros():
    lista = [5, 4, 3, 2, 1]
    return lista

def calcular(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma

def imprimir(result):
    print(result)

def principal():
    num = numeros()
    resultado = calcular(num)
    imprimir(resultado)

principal()