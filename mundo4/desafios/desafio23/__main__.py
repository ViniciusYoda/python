from poligono import Quadrado, Circulo
from rich import print

def main():
    q = Quadrado(5)
    print(f"Perímetro do quadrado: {q.perimetoro()}")
    print(f"Área do quadrado: {q.area()}")
    
    c = Circulo(3)
    print(f"Perímetro do círculo: {c.perimetoro()}")
    print(f"Área do círculo: {c.area()}")
    
    
if __name__ == "__main__":
    main()