def soma_item(lista):
    soma= 0
    for i in lista:
        soma += i
    return soma
    
def soma_item_recursivo(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + soma_item_recursivo(lista[1:])
    
#principal
print(soma_item([1, 3, 5, 7, 9]))
print(soma_item_recursivo([1, 3, 5, 7, 9]))