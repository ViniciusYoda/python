def periodo_dias():
    dias = int(input('Quantos dias você quer ver? '))
    return dias

def periodo_semanas():
    semanas = int(input('Quantas semanas? '))
    return semanas

def periodo(dia, semana):
    semanas = []
    for i in range(dia):
        dias = []
        for j in range(semana):
            dias.append(semana)
    semanas.append(dias)
    return semanas

def coletar(dia, semana):
    temperatura = []
    for i in range(semana):
        tempSemana = []
        for j in range(dia):
            tempDia = float(input('Temperatura: '))
            tempSemana.append(tempDia)
    temperatura.append(tempSemana)
    return temperatura

def maior_temperatura(matriz):
    maior_temperatura = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
           if i == 0 and j == 0:
                maior_temperatura = matriz[i][j]
                if matriz[i][j] > maior_temperatura:
                    maior_temperatura = matriz[i][j]
    return maior_temperatura 

def menor_temperatura(matriz):
    menor_temperatura = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == 0 and j == 0:
                menor_temperatura = matriz[i][j]
                if matriz[i][j] < menor_temperatura:
                    menor_temperatura = matriz[i][j]
    return menor_temperatura    

def temperatura_negativa(matriz):
    tempNegativo = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] < 0:
                tempNegativo.append(matriz[i][j])
    return tempNegativo

def media_temperatura(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma += matriz[i][j]
            media = soma / len(matriz)
    return media



def principal():
    dia = periodo_dias()
    semana = periodo_semanas()
    matriz = periodo(dia, semana)
    temperatura = coletar(dia, semana)
    matriz.append(temperatura)
    maior_temperatura(matriz)
    menor_temperatura(matriz)
    temperatura_negativa(matriz)
    media_temperatura(matriz)

principal()