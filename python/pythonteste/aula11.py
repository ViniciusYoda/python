print('\033[1;31;44mOlá Mundo\033[m')
print('\033[1;30;44mOlá Mundo\033[m')
print('\033[1;31;45mOlá Mundo\033[m')
print('\033[1;31;40mOlá Mundo\033[m')
print('\033[1;31;41mOlá Mundo\033[m')
print('\033[1;31;42mOlá Mundo\033[m')
print('\033[1;31;43mOlá Mundo\033[m')
print('\033[1;31;46mOlá Mundo\033[m')
print('\033[1;31;47mOlá Mundo\033[m')
print('\033[0;37;44mOlá Mundo\033[m')
nome = 'Bruno'
cores = {'limpa': '\033[m', 
         'azul':'\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}
print('Olá {}{}{}'.format(cores['amarelo'], nome, cores['limpa']))