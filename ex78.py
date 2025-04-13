numeros = []
for i in range(5):
    valor = int(input(f"Digite o {i + 1}º valor: "))
    numeros.append(valor)
maior_valor = max(numeros)
menor_valor = min(numeros)
print(f"\nVocê digitou os valores: {numeros}")
print(f"O maior valor é {maior_valor} nas posições ", end="")
for i, v in enumerate(numeros):
    if v == maior_valor:
        print(f"{i} ", end="")
print(f"\nO menor valor é {menor_valor} nas posições ", end="")
for i, v in enumerate(numeros):
    if v == menor_valor:
        print(f"{i} ", end="")