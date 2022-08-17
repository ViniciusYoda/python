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

def principal():
    t = tamanho_lista()
    lista = criar_lista(t)
    imprimir_lista(lista)

# programa principal
principal()
