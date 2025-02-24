import random
p = input('Primeiro aluno: ')
s = input('Segundo aluno: ')
t = input('Terceiro aluno: ')
q = input('Quarto aluno: ')
l = [p, s, t, q]
c = random.choice(l)
print(f'O aluno escolhido foi: {c}')