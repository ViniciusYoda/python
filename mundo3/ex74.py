from random import randint
n = (randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5))
print('Os números sorteados foram:', n)
print(f'O maior número sorteado foi {max(n)}')
print(f'O menor número sorteado foi {min(n)}')
print('FIM')