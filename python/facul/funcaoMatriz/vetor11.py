def matriz_linha():
    linha = int(input('Quantas linhas? '))
    return linha

def matriz_coluna():
    coluna = int(input('Quantas colunas? '))
    return coluna

def criar_matriz(linha, coluna):
    matriz = []
    matriz.append(linha)
    matriz.append(coluna)
    return matriz
    
def preencher(num, matriz):
    matriz.append(num)
    
def imprimir(res):
    print(res)
    
linha = matriz_linha()
coluna = matriz_coluna()
matriz = criar_matriz(linha, coluna)
numeros = preencher(20, matriz)
imprimir(numeros)

    
