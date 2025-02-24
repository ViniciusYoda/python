import random
p = input('Primeiro aluno: ')
s = input('Segundo aluno: ')
t = input('Terceiro aluno: ')
q = input('Quarto aluno: ')
l = [p, s, t, q]
o = random.shuffle(l)
print(f'A ordem de apresentação será: {o}')