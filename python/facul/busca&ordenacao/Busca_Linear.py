#Busca Linear

def busca_linear(valor, lista):
    for item in lista:
        if item == valor:
            return item #retorna o item encontrado
    return None

def busca_linear2(valor, lista):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return None  

def busca_linear3(valor, lista):
    for i, item in enumerate(lista):
        if item == valor:
            return i
    return None   

#to do
'''
1) Crie uma função (busca_linear), porém retornando -1 como resposta para o valor encontrado. A ideia é manter a coerência do tipo de valor retornando em todos os casos, imprescindivel em diversar linguagens

2) Crie uma função (busca_linear), porém, que o valor de retorno seja uma lista com os indices de todos os itens iguais ao valor buscado
'''   

#Programa Principal
lista = [3, 6, 5, 8, 0, 8, 2]
print(f'Item: {busca_linear(8, lista)}')
print(f'Indice: {busca_linear2(8, lista)}')
print(f'Index: {busca_linear3(0, lista)}')

menu = ['lanches', 'pizzas', 'saladas', 'bebidas']
for index, item in enumerate(menu):
    print(index, item)
