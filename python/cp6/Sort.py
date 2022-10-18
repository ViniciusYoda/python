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
        esquerdo = lista[:meio]
        direito = lista[meio:]

        mergeSort(esquerdo)
        mergeSort(direito)

        i = j = k = 0

        while i < len(esquerdo) and j < len(direito):
            if esquerdo[i] <= direito[j]:
                lista[k] = esquerdo[i]
                i+= 1
            else:
                lista[k] = direito[j]
                j += 1
            k += 1

        while j < len(esquerdo):
            lista[k] = esquerdo[i]
            i += 1
            k == 1

        while j < len(direito):
            lista[k] = direito[j]
            j += 1
            k == 1
    return lista


def dezMil():
    lista = []
    for i in range(random.randint(1, 10000)):
        lista.append(i)
        lista[1:10000]
    return lista

def cemMil():
    lista = []
    for i in range(random.randint(1, 100000)):
        lista.append(i)
    return lista

def quiMil():
    lista = []
    for i in range(random.randint(1, 500000)):
        lista.append(i)
    return lista

def umMilhao():
    lista = []
    for i in range(random.randint(1, 1000000)):
        lista.append(i)
    return lista

def cincoMilhao():
    lista = []
    for i in range(random.randint(1, 5000000)):
        lista.append(i)
    return lista



#def get_time(arg):
    inicio = time.time()
    time.sleep(arg)
    fim = time.time()
    return fim-inicio

def principal():
    dm = dezMil()
    cm = cemMil()
    qm = quiMil()
    umm = umMilhao()
    cmm = cincoMilhao()
    bsdm = bubbleSort(dm)
    bscm = bubbleSort(cm)
    bsqm = bubbleSort(qm)
    bsumm = bubbleSort(umm)
    bscmm = bubbleSort(cmm)
    print(dm)
    


principal()