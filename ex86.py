matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f"Digite um valor para [{linha}, {coluna}]: "))

print("\nMatriz formatada:")
for linha in matriz:
    for valor in linha:
        print(f"[{valor:^5}]", end="")
    print()