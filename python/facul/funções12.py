def obter_altura():
    alt = float(input('Digite a sua altura: '))
    return alt

def obter_sexo():
    sexo = str(input('Digite o seu sexo: [M / H] ')).upper()[0]
    return sexo

def calcular_peso(alt, sexo):
    if sexo in 'H':
        p = 72.7 * alt - 58
    elif sexo in 'M':
        p = 62.1 * alt - 44.7
    return p 

def principal():
    alt = obter_altura()
    sexo = obter_sexo()
    print(calcular_peso(alt, sexo))

principal()

