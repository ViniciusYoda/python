total = 0
preco = float(input("Preço do item: "))
while preco != -1:
    total += preco
    preco = float(input("Preço do item: "))
print(f"Total de compra: R$ {total:.2f}")