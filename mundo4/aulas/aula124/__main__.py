from ex124 import ContaBancaria

def main():
    c1 = ContaBancaria(123, "Gustavo", 3000)
    c1.depositar(500)
    c1._titular = "Gustavo Oliveira"
    c1.sacar(27000)
    print(c1)

if __name__ == "__main__":
    main()