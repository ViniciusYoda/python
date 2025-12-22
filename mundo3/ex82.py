numeros = []

pares = []
impares = []

while True:
    numero = int(input("Digite um número (ou -1 para sair): "))
    if numero == -1:
        break
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Lista completa:", numeros)
print("Lista de pares:", pares)
print("Lista de ímpares:", impares)