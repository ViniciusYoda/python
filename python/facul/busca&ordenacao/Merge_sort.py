def merge_sort(lista):
    if len(lista) > 1:

        #encontrando o meio da lista
        meio = len(lista) // 2

        #dividindo a lista em duas
        esquerdo = lista[:meio]
        direito = lista[meio:]
        #ordenando a primeira lista
        merge_sort(esquerdo)

        #ordenando a segunda lista
        merge_sort(direito)

        i = j = k = 0


        while i < len(esquerdo) and j < len(direito):
            if esquerdo[i] <= direito[j]:
                lista[j] = esquerdo[i]
                i+1
            else:
                lista[k] = direito[j]
                j+=1
                k+=1

            #verificando os elementos da lista esq
            while i < len(esquerdo):
                lista[k] = esquerdo[i]
                i+=1
                k+=1

                #verificando os elementos da lista dir
            while j < len(direito):
                lista[k] = direito[j]
                j+=1
                k+=1
    return lista

lista = [12, 11, 13, 5, 6, 7]
print(f'Lista:{lista}')
merge_sort(lista)
print(f'Lista ordenada: {lista}')

