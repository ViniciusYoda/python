def percorrrer_lista(lista):
    print('Percorrendo uma lista')
    i = 0
    while i < len(lista):
        print(f'Elemento: {lista[i]}')
        i+=1

#principal
lista = [1,2,3,4,5]
percorrrer_lista(lista)