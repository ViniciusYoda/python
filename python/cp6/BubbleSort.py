'''
Bubble sort ordena a lista elemento por elemento.
'''

def bubbleSort(array):
    for final in range(len(array), 0, -1):
        exchanging = False
        for current in range(0, final - 1):
            if array[current] > array[current + 1]:
                array[current], array[current + 1] = array[current + 1], array[current]
                exchanging = True
        if not exchanging:
            break

array = [8, 7, 5, 3, 1, 2, 9, 6, 4]
bubbleSort(array)
print(array)