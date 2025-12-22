def ajuda(comando):
    """Exibe o manual de ajuda do Python para o comando informado."""
    titulo(f"Acessando o manual do comando '{comando}'", cor=4)
    print('\033[7;30m', end='')  
    help(comando)
    print('\033[m', end='')  


def titulo(msg, cor=0):
    """Exibe um título formatado com cores."""
    tamanhos = len(msg) + 4
    print(f'\033[{30+cor}m', end='') 
    print('~' * tamanhos)
    print(f'  {msg}')
    print('~' * tamanhos)
    print('\033[m', end='')  

while True:
    titulo("SISTEMA DE AJUDA PyHELP", cor=2)
    comando = input("Função ou Biblioteca > ").strip()
    if comando.lower() == 'fim':
        titulo("ATÉ LOGO!", cor=1)
        break
    else:
        ajuda(comando)