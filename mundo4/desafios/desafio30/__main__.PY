from classes030 import *

def main():
    c = Credencial()
    c.senha = 'yoda'
    print(c.senha)
    validacao = c.validar('yoda')
    print(f"Senha valida: {validacao}")

if __name__ == "__main__":
    main()