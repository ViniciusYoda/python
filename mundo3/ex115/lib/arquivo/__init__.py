import os

CAMINHO = r"C:\Users\Luana\Documents\GitHub\Python\ex115"

def arquivoExiste(nome):
    os.chdir(CAMINHO)
    try:
        with open(nome, 'rt'):
            pass
    except FileNotFoundError:
        return False
    else:
        return True

def criar_arquivo(nome):
    try:
        # Garante que o diretório existe antes de tentar criar o arquivo
        os.makedirs(CAMINHO, exist_ok=True)
        caminho_arquivo = os.path.join(CAMINHO, nome)
        with open(caminho_arquivo, 'wt+'):
            pass
    except Exception as erro:
        print(f'Houve um erro na criação do arquivo: {erro}')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def adicionar_dados(nome_arquivo):
    try:
        with open(nome_arquivo, 'at') as arquivo:
            nome = str(input('Nome: '))
            idade = int(input('Idade: '))
            arquivo.write(f'{nome};{idade}\n')
            print(f'Novo registro de {nome} adicionado.')
    except:
        print('Houve um erro ao escrever no arquivo!')

def ver_dados(nome_arquivo):
    try:
        with open(nome_arquivo, 'rt') as arquivo:
            print('PESSOAS CADASTRADAS'.center(40))
            for linha_arquivo in arquivo:
                dado = linha_arquivo.strip().split(';')
                if len(dado) == 2:
                    print(f'{dado[0]:<30}{dado[1]:>3} anos')
    except:
        print('Houve um erro ao ler o arquivo!')
    finally:
        print('Fim do arquivo!')
