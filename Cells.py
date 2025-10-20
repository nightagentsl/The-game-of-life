import random
import os
import time
import sys

if os.name == "nt":  # La c'est pour Windows
    import msvcrt

    def get_key():
        # Retourne une touche pressée ou None s'il n'y en a pas #
        if msvcrt.kbhit():
            return msvcrt.getch().decode("utf-8").lower()
        return None
else:  # C'est pas analysé sur window et c'est normal parce que c'est pour Linux.
    import sys, termios, tty, select

    def get_key():
        # Retourne quand une touche est pressée #
        dr, _, _ = select.select([sys.stdin], [], [], 0)
        if dr:
            return sys.stdin.read(1).lower()
        return None

class Cell:
    def __init__(self, alive=False):
        self.alive = alive

    def __repr__(self):
        return "​◘" if self.alive else "♦"

class Universe:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.generate_random_grid()

    def generate_random_grid(self):
        # Crée une grille aléatoire de cellules vivantes/mortes #
        self.grid = [
            [Cell(random.choice([True, False])) for _ in range(self.width)]
            for _ in range(self.height)
        ]

    def display(self, generation, pause=False):
        # Affiche la grille dans la console #
        os.system("cls" if os.name == "nt" else "clear") # Ça nettoie la console
        print(f"Génération : {generation}\n")
        for row in self.grid:
            print(" ".join(str(cell) for cell in row))
        print()
        if pause:
            print("⏸ Jeu en pause — appuyez sur [ESPACE] pour reprendre, [n] pour nouvelle grille, [q] pour quitter.")
        else:
            print("(Appuyez sur [ESPACE] pour mettre en pause)")

    def count_neighbors(self, x, y):
        """Compte le nombre de voisins vivants autour d’une cellule"""
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1), (1, 0), (1, 1),
        ]
        count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.height and 0 <= ny < self.width:
                if self.grid[nx][ny].alive:
                    count += 1
        return count

    def next_generation(self):
        """Applique les règles du jeu de la vie pour passer à la génération suivante"""
        new_grid = [[Cell() for _ in range(self.width)] for _ in range(self.height)]
        for x in range(self.height):
            for y in range(self.width):
                alive = self.grid[x][y].alive
                neighbors = self.count_neighbors(x, y)
                if alive and neighbors in (2, 3):
                    new_grid[x][y].alive = True
                elif not alive and neighbors == 3:
                    new_grid[x][y].alive = True
        self.grid = new_grid

def demander_taille():
    """Demande la taille de la grille à l'utilisateur"""
    while True:
        try:
            width = int(input("Entrez la largeur de la grille : "))
            height = int(input("Entrez la hauteur de la grille : "))
            return width, height
        except ValueError:
            print("⚠️ Veuillez entrer des nombres entiers valides.\n")


# --- Programme principal ---
if __name__ == "__main__":
    while True:  # boucle générale 
        width, height = demander_taille()
        universe = Universe(width, height)
        generation = 0
        paused = False

        while True:  
            universe.display(generation, paused)

            key = get_key()
            if key == " ":
                paused = not paused
            elif key == "n":
                break  
            elif key == "q":
                print("👋 Fin du programme.")
                sys.exit()

            if not paused:
                time.sleep(0.7)
                generation += 1
                universe.next_generation()
            else:
                time.sleep(100)