def merge_sort(lista):
    if len(lista) > 1:

        #encontrando o meio da lista
        meio = len(lista) // 2

        #dividindo a lista em duas
        esq = lista[:meio]
        dir = lista[meio:]
        #ordenando a primeira lista
        merge_sort(esq)

        #ordenando a segunda lista
        merge_sort(dir)

        i = j = k = 0


        while i < len(esq) and j < len(dir):
            if esq[i] <= dir[j]:
                lista[j] = esq[i]
                i+1
            else:
                lista[k] = dir[j]
                j+=1
                k+=1

            #verificando os elementos da lista esq
            while i < len(esq):
                lista[k] = esq[i]
                i+=1
                k+=1

                #verificando os elementos da lista dir
            while j < len(dir):
                lista[k] = dir[j]
                j+=1
                k+=1

lista = [12, 11, 13, 5, 6, 7]
print(f'Lista:{lista}')
merge_sort(lista)
print(f'Lista ordenada: {lista}')

