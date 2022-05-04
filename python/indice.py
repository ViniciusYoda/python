#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

num = int(input('Digite um número entre zero a dez: '))

while (num >= 0 and num <=10):
    print('Número certo')
    if num > 10:
        print(num = int(input('Digite um número entre zero a dez: ')))
    else:
        print('Jogo corrento')
        break
