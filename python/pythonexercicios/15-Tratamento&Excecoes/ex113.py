def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: por favvor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompda pelo usuário.\033[m')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: por favvor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompda pelo usuário.\033[m')
            return 0
        else:
            return n           

n1 = leiaInt('Digite um valor: ')
n2 = leiaFloat('Digite um valor: ')
print(f'O valor digitado foi: {n1} e {n2}')