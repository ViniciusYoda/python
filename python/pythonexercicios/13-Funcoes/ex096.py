def calcularArea(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura}X{comprimento} é de {a}m².')
    
print('Area')
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
calcularArea(l, c)