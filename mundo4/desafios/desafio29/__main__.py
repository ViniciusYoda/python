from classes029 import *

def main():
    meudiaro = Diario()
    meudiaro.escrever("Primeiro contanto")
    try:
        meudiaro.ler('CeV!@')
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()