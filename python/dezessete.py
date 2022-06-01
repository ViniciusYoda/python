from pickle import TRUE


total = 0
quero_comprar = TRUE
while quero_comprar:
    preco = float(input("Preço: "))
    total += preco
    opcao = input("Quer continuar comprando? [s/n]")
    if opcao != "s":
        quero_comprar = False
print(f"Total de compra: {total:.2f}")