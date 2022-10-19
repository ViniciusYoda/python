from heapq import merge
import time
import random

def bubbleSort(lista):
    '''
    Função que ordena a lista um por um
    '''
    for c in range(len(lista), 0, -1):
        ordenado = False
        for i in range(0, c - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                ordenado = True
        if not ordenado:
            break
    return lista

def selectionSort(lista):
    for i in range(0, len(lista)):
        min_index = i

        for r in range(i, len(lista)):
            if lista[r] < lista[min_index]:
                min_index = r
        
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista

def insertionSort(lista):
    for i in range(1, len(lista)):
        pivo = lista[i]
        j = i - 1
        while j >= 0 and pivo < lista[j]:
            lista[j+1] = lista[j]
            j-=1
        lista[j+1] = pivo
    return lista

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

def quickSort(lista):
    tamanho = len(lista)
    if tamanho <= 1:
        return lista
    else:
        pivo = lista.pop()

    items_greater = []
    items_lower = []

    for i in lista:
        if i > pivo:
            items_greater.append(i)

        else:
            items_lower.append(i)

    return quickSort(items_lower) + [pivo] + quickSort(items_greater)

def get_time(arg):
    inicio = time.time()
    time.sleep(arg)
    fim = time.time()
    return fim-inicio

def principal():
   pass
    
