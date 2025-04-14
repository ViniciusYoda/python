matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f"Digite um valor para [{linha}, {coluna}]: "))

print("\nMatriz:")
for linha in matriz:
    print("[", " ".join(f"{num:^5}" for num in linha), "]")

soma_pares = sum(num for linha in matriz for num in linha if num % 2 == 0)
soma_terceira_coluna = sum(matriz[linha][2] for linha in range(3))
maior_segunda_linha = max(matriz[1])

print(f"\nA) A soma de todos os valores pares digitados: {soma_pares}")
print(f"B) A soma dos valores da terceira coluna: {soma_terceira_coluna}")
print(f"C) O maior valor da segunda linha: {maior_segunda_linha}")