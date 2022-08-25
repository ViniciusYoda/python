def numeros():
    lista = [5, 4, 3, 2, 1]
    return lista

def media(lista):
    soma = 0
    for media in lista:
        soma += media
    return media / len(lista)

def imprimir(result):
    print(result)

def principal():
    num = numeros()
    resultado = media(num)
    imprimir(resultado)

principal()