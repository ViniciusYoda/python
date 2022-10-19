
def mergeSort(array):
    aux = array[:]
    sort_half(array, 0, len(array) - 1)

def sort_half(array, aux, start, end):

    middle = (start + end) // 2
    sort_half(array, aux, start, middle)
    sort_half(array, aux, middle + 1, end)

    merge(array, aux, start, end)

def merge(array, aux, start, end):
    left = start
    left_end = (start + end) // 2

    right = left_end + 1
    right_end = end

    position = start

    for position in range(start, end + 1):

        if left > left_end:
            aux[position] = array[right]
            right += 1

        elif right > right_end:
            aux[position] = array[left]
            left += 1


        elif array[left] < array[right]:
            aux[position] = array[left]
            left += 1


        else:
            aux[position] = array[right]
            right += 1

    for k in range(start, end + 1):
        array[k] = aux[k]


    
import random
array = [random.randint(0, 100) for i in range(1000)]
copy_array = array[:]
import time

start = time.time()
mergeSort(array)
end = time.time()
print(array)

assert array == sorted(copy_array)