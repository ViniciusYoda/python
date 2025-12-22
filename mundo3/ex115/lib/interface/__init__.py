def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
        except ValueError:
            print("Erro: Por favor, digite um número inteiro válido.")
        except KeyboardInterrupt:
            print("\nEntrada de dados interrompida pelo usuário.")
            return 0
        else:
            return valor
        
def linha(tam = 42):
    """Função para criar uma linha"""
    return '-' * tam    

def cabecalho(txt):
    """Função para criar um cabeçalho"""
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    """Função para criar um menu"""
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opcao = leiaInt('\033[32mSua Opção: \033[m')
    return opcao