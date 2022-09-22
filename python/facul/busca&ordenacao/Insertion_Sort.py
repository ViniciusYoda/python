#Insertion Sort

def insertion_sort(lista):
    for i in range(1, len(lista)):
        pivo = lista[i]
        j = i - 1
        while j >= 0 and pivo < lista[j]:
            lista[j+1] = lista[j]
            j-=1
        lista[j+1] = pivo

lista = [12, 11, 13, 5, 6]
insertion_sort(lista)
