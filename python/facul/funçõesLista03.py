def tamanho_lista():
    t = int(input('Qual é o tamanho da lista? '))
    return t

def criar_lista(t):
    lista = list(range(t))
    i = 0
    while i < t:
        lista[i] = int(input("Número: "))
        i+=1
    return lista
    

def imprimir_lista(lista):
    for i in lista:
        print(f'Elemento: {i}')

def imprimir_pares(lista):
    for i in lista:
        if i % 2 == 0:
            print(f'Números pares: {i}')

def imprimir_impares(lista):
    for i in lista:
        if i % 2 != 0:
            print(f'Números ímpares: {i}')

def adicionar_pares(lista):
    lista_pares = []
    for i in lista:
        if i%2 == 0:
            lista_pares.append(i)
    return lista_pares

def adicionar_impares(lista):
    lista_impares = []
    for i in lista:
        if i%2 == 1:
            lista_impares.append(i)
    return lista_impares

def buscar_elemento(lista):
    busca = int(input('Por qual elemento você está procurando? '))
    if busca in lista:
        print(f'O número {busca} está na lista')
    else:
        print(f'O número {busca} não está na lista')
    return busca


def principal():
    t = tamanho_lista()
    lista = criar_lista(t)
    imprimir_lista(lista)
    imprimir_pares(lista)
    lista_pares = adicionar_pares(lista)
    imprimir_lista(lista_pares)
    imprimir_impares(lista)
    lista_impares = adicionar_impares(lista)
    imprimir_lista(lista_impares)
    buscar_elemento(lista)

# programa principal
principal()
