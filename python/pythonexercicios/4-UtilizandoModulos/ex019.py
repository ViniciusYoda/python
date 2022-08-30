import random
ua = input('Primeiro aluno: ')
da = input('Segundo aluno: ')
ta = input('Terceiro aluno: ')
qa = input('Quarto aluno: ')
lista = [ua, da, ta, qa]
al = random.choice(lista)
print('O aluno escolhido foi {}'.format(al))