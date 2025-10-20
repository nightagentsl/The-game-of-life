import random
import os

class Cell:
    def __init__(self, alive=False):
        self.alive = alive

    def __repr__(self):
        return "💭​​" if self.alive else "💀​"

class Universe:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # Création d'une grille de cellules aléatoires
        self.grid = [[Cell(random.choice([True, False])) for _ in range(width)] for _ in range(height)]

    def display(self):
        os.system("cls" if os.name == "nt" else "clear")  # nettoie le terminal
        for row in self.grid:
            print(" ".join(str(cell) for cell in row))
        print()

    def count_neighbors(self, x, y):
        """Compte les cellules vivantes autour d'une cellule donnée"""
        directions = [(-1,-1), (-1,0), (-1,1),
                      (0,-1),          (0,1),
                      (1,-1), (1,0), (1,1)]
        count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.height and 0 <= ny < self.width:
                if self.grid[nx][ny].alive:
                    count += 1
        return count

    def next_generation(self):
        """Crée la génération suivante selon les règles de Conway"""
        new_grid = [[Cell() for _ in range(self.width)] for _ in range(self.height)]

        for x in range(self.height):
            for y in range(self.width):
                alive = self.grid[x][y].alive
                neighbors = self.count_neighbors(x, y)

                # Règles de Conway
                if alive and neighbors in (2, 3):
                    new_grid[x][y].alive = True
                elif not alive and neighbors == 3:
                    new_grid[x][y].alive = True
                else:
                    new_grid[x][y].alive = False

        self.grid = new_grid
        
        
def askSize():
    # Demande la taille de la grille à l'utilisateur #
    
    while True:
        try:
            width = int(input("Entrez la largeur de la grille : "))
            height = int(input("Entrez la hauteur de la grille : "))
            return width, height
        except ValueError:
            print("⚠️ Veuillez entrer des nombres entiers valides.\n")


# Programme principal #
if __name__ == "__main__":
    while True:
        width, height = askSize()
        universe = Universe(width, height)
        generation = 0

        while True:
            universe.display()
            print(f"Génération : {generation}")
            print("\nOptions :")
            print("1 - Génération suivante")
            print("2 - Nouvelle grille")
            print("3 - Quitter")

            choix = input("\nVotre choix : ")

            if choix == "1":
                universe.next_generation()
                generation += 1
            elif choix == "2":
                break
            elif choix == "3":
                print("Au revoir 👋")
                exit()
            else:
                print("Choix invalide. Veuillez entrer 1, 2 ou 3.")
                input("Appuyez sur Entrée pour continuer...")