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

def dezMil():
    lista = []
    for i in range(random.randint(10000)):
        lista.append(i)
    return lista

def cemMil():
    lista = []
    for i in range(random.randint(100000)):
        lista.append(i)
    return lista

def quiMil():
    lista = []
    for i in range(random.randint(500000)):
        lista.append(i)
    return lista

def umMilhao():
    lista = []
    for i in range(random.randint(1000000)):
        lista.append(i)
    return lista

def cincoMilhao():
    lista = []
    for i in range(random.randint(10000)):
        lista.append(i)
    return lista



def get_time(arg):
    inicio = time.time()
    time.sleep(arg)
    fim = time.time()
    return fim-inicio

def principal():
    dezMil = dezMil()
    bs = bubbleSort(dezMil)
    get_time(bs)


principal()