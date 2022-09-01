credito = float(input("Qual seu credito: "))
total = 0
preco = float(input("Preço do item: "))
while credito >= preco:
    total += preco
    credito -= preco
    preco = float(input("Preço do item: "))
    
print(f"Total de compra: R$ {total:.2f}")
print(f"Credito restante: R$ {credito:.2f}")