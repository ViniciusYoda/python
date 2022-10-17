'''
selection sort pega o menor número em uma lista e coloca no ínico na lista ordenado
'''

def selectionSort(array):
    for index in range(0, len(array)):
        min_index = index

        for right in range(index, len(array)):
            if array[right] < array[min_index]:
                min_index = right
        
        array[index], array[min_index] = array[min_index], array[index]

array = [8, 7, 5, 3, 1, 2, 9, 6, 4]
selectionSort(array)
print(array)