r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo. ', end='')
    if r1 == r2 == r3:
        print('O triângulo formam equilátero')
    elif r1 != r2 and r1 != r3:
        print('O triângulo formam um escaleno')
    else: 
        print('O triângulo formam um isósceles')
else:
    print('Os segmentos acima não pode formar um triângulo')