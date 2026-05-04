import cafeteria

def main():
    cafe = cafeteria.Cafe()
    cafe.preparar()
    
    print("\n")
    
    cha = cafeteria.Cha()
    cha.preparar()
    
    print("\n")
    
    leite = cafeteria.Leite()
    leite.preparar()

if __name__ == "__main__":
    main()