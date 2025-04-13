numeros = []
while True:
    numero = int(input("Digite um número: "))
    if numero not in numeros:
        numeros.append(numero)
        print("Número adicionado com sucesso!")
    else:
        print("Número duplicado! Não será adicionado.")

    continuar = input("Deseja continuar? [S/N]: ").strip().upper()
    if continuar == 'N':
        break

numeros.sort()
print("Os valores únicos digitados, em ordem crescente, são:", numeros)