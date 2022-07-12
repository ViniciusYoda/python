#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';
nome = str(input('Qual é seu nome?: '))


while ( len(nome) <=  3 ):
	nome = str(input('Qual é seu nome?: '))

else: 
    print('Primeiro passo feito')

idade = int(input('Qual é a sua idade?: '))

if idade >= 0 and idade <= 150:
    print('Pode seguir em frente')
else: 
    print('Digite a idade válida1')
    idade = int(input('Qual é a sua idade?: '))

salario = float(input('Qual é seu salário?: '))

if salario < 0:
    print('Salário inválido! Coloque outro valor, ou se você não tiver um emprego, procure um!')
    salario = float(input('Qual é seu salário?: '))
else:
    print('Continue assim!')

sexo = str(input('Qual é seu sexo? (f/m) '))

if sexo != 'f' and sexo != 'm':
    print('Infelizmente, ainda não aceitamos outros tipos de sexo.')
    sexo = str(input('Qual é seu sexo? (f/m) '))

else: 
    print('Continua a nadar')

estadoCivil = str(input('Qual é seu estado civil?: '))

if estadoCivil != 's' and estadoCivil != 'v' and estadoCivil != 'c' and estadoCivil != 'd':
    print('Digite um estado civil válido!')
    estadoCivil = str(input('Qual é seu estado civil?: '))

else:
    print('concluido com sucesso!')




