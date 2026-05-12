from transportes import *
from rich import print, inspect
from rich.table import Table

def main():
    dist = 5
    
    viagem = [Moto(dist), Caminhao(dist), Drone(dist)]
    
    tabela = Table(title="Tabela de Fretes")
    tabela.add_column("Distancia")
    tabela.add_column("Tipo")
    tabela.add_column("Frete")
    
    for item in viagem:
        tabela.add_row(f"{dist}", f"{type(item).__name__}", f"{item.calcular_frete()}")
        
    print(tabela)
    
if __name__ == "__main__":
    main()