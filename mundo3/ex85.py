numeros = [[], []] 

for i in range(7):
    valor = int(input(f"Digite o {i + 1}º valor: "))
    if valor % 2 == 0:
        numeros[0].append(valor) 
    else:
        numeros[1].append(valor) 

numeros[0].sort()
numeros[1].sort()

print(f"Os valores pares digitados foram: {numeros[0]}")
print(f"Os valores ímpares digitados foram: {numeros[1]}")