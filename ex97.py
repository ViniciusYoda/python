def escreva(texto):
    tamanho = len(texto) + 4
    print('~' * tamanho)
    print(f'  {texto}')
    print('~' * tamanho)

escreva("Olá, Mundo!")
escreva("Python é incrível!")