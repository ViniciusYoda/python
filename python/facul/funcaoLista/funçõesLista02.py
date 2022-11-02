lista = [2, 10, 5, -3, 20]

def imprime_elemntos(lista):
    i = 0
    while i < len(lista):
        print(f'Elemento: {lista[i]}')
        i+=1
    lista[0] = 2000

#principal
imprime_elemntos(lista)
imprime_elemntos(lista)

