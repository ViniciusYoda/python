def selection_sort(lista):
    for i in range(len(lista)):
        min_index = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index]
    return lista

lista = [-2, 50, 23, 0, 111, -9, 88]
print(selection_sort(lista))