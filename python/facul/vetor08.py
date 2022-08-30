def vetores():
    numeros = [1,2,3,4,5,6,7,8,9]
    return  numeros

def vetor():
    numero = 5
    return numero

def verificacao(numero, numeros):
    for numero in numeros: 
        if numero in numeros:
            print(f'O número {numero} foi encontrando na lista')
        else: 
            print(f'O número {numero} não foi encontrando na lista')
            
numero = vetor()
numeros = vetores()
verificacao(numero, numeros)