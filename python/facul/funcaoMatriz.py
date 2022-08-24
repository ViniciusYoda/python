def criar_matriz(n_linhas, n_colunas, valor):
    '''
    PArâmetros:
    (int, int, int) -> matriz(lista de listas)

    Cria uma matriz e retorna com n_linhas e n_colunas
    em que cada elemento é igual ao valor passado por parÂmetro

    Retorno:
    Retorna uma matriz com n_linahs e n_colunas
    '''
    matriz = [] #lista vazia
    for i in range(n_linhas):
        #cria a linha i
        linha = [] #lista vazia
        for j in range(n_colunas):
            linha.append(valor)

        #adiciona a linha na matrix
        matriz.append(linha)

    return matriz


#programa principal
matriz = criar_matriz(3, 3, 0)
matriz[1][1] = 100
print(matriz[1][1])

