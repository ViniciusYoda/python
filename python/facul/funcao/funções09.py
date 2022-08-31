# Faça uma função que recebe por parâmetro o raio (R) de uma esfera e calcula o seu volume, 
# onde o volume é dado por: v = (4/3).π.R3.

import math

def raio():
    r = int(input('Número do raio: '))
    return r

def calcular_esfera(r):
    v = (4/3) * math.pi * r ** 3
    print(f'{v:.2}')
    return v

def principal():
    r = raio()
    calcular_esfera(r)

principal()