numeros = []

while True:
    numero = int(input("Digite um número (ou digite -1 para parar): "))
    if numero == -1:  
        break
    numeros.append(numero)

quantidade = len(numeros)

numeros_ordenados = sorted(numeros, reverse=True)

tem_cinco = 5 in numeros

print(f"\nA) Quantidade de números digitados: {quantidade}")
print(f"B) Lista de valores em ordem decrescente: {numeros_ordenados}")
if tem_cinco:
    print("C) O valor 5 foi digitado e está na lista.")
else:
    print("C) O valor 5 não foi digitado e não está na lista.")