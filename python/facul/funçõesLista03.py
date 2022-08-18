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
    par = int(input('Digite um número par: '))
    if par % 2 == 0:
        lista.append(par)
    else:
        print('Número não adicionado')
    return par

def adicionar_impares(lista):
    impar = int(input('Digite um número ímpar: '))
    if impar % 2 != 0:
        lista.append(impar)
    else:
        print('Número não adicionado')
    return impar

def buscar_elemento(lista):
    busca = int(input('Por qual elemento você está procurando? '))
    if busca in lista:
        print(f'O núemro {busca} está na lista')
    else:
        print(f'O número {busca} não está na lista')
    return busca


def principal():
    t = tamanho_lista()
    lista = criar_lista(t)
    imprimir_lista(lista)
    imprimir_pares(lista)
    imprimir_impares(lista)
    adicionar_pares(lista)
    adicionar_impares(lista)
    imprimir_lista(lista)
    buscar_elemento(lista)

# programa principal
principal()
