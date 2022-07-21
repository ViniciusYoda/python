from random import randint
numero = (randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5))
print("OS valores sorteados foram: ", end='')
for n in numero:
    print(f'{n} ', end="")
print(f"\nO maior valor sorteado foi {max(numero)}")
print(f"O menor valor sorteado foi {min(numero)}")