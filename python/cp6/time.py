import time

def get_time(lista):
    inicio = mergeSort(lista).time()
    time.sleep(lista)
    fim = mergeSort(lista).time()
    return fim-inicio

def mergeSort(lista):
    if len(lista) > 1:

        meio = len(lista) // 2
        left = lista[:meio]
        right = lista[meio:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lista[k] = left[i]
                i += 1
            else:
                lista[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lista[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lista[k] = right[j]
            j += 1
            k += 1

    return lista

lista = [4, 3, 2, 1]

merge = mergeSort(lista)

dif = get_time(lista)
print(f'Dif: {dif:.2f}')