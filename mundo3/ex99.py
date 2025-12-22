def maior(*numeros):
    if numeros:
        maior_numero = max(numeros)
        print(f"Analisando os valores {numeros}, o maior valor é {maior_numero}.")
    else:
        print("Nenhum número foi informado.")

maior(2, 5, 8, 1, 4)
maior(10, 20, 30)
maior()