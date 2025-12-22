def area(largura, comprimento):
    terreno_area = largura * comprimento
    print(f"A área do terreno {largura}x{comprimento} é de {terreno_area}m².")

print("Controle de Terrenos")
print("-" * 20)
larg = float(input("Largura (m): "))
comp = float(input("Comprimento (m): "))
area(larg, comp)