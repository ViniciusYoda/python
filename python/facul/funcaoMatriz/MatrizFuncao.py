''''''
def cria_matriz(n_linhas, n_colunas):
    '''
    (int, int) --> matriz númerica
    '''
    matriz = []
    for i in range(n_linhas):
        linha = []
        for j in range(n_colunas):
            n = int((input('item: ')))
            linha.append(n)
        matriz.append(linha)
    return matriz
    
def somaItens(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma += matriz[i][j]
    return soma

def principal():
    matriz = cria_matriz(3, 3)
    soma = somaItens(matriz)
    print(f'Soma: {soma}')
    
principal()