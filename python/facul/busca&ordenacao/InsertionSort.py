'''
Verifica o item da esquerda, se for maior que da direita, ele troca, até ordenar
'''



def insertionSort(array):
    compares, assigns = 0, 0
    for p in range(0, len(array)):
        current_element = array[p]

        if p > 0:
            compares += 1

        while p > 0 and array[p - 1] > current_element:
            array[p] = array[p - 1]

            assigns +=1
            p -= 1

        array[p] = current_element
        assigns += 1
    print(compares, assigns)

array = [8, 7, 5, 3, 1, 2, 9, 6, 4]
copy_array = array[:]
insertionSort(array)
print(array)

assert array == sorted(copy_array)