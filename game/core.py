import random
import os
import time
import sys

# --- Détection du système pour la gestion des touches ---
if os.name == "nt":  # Windows
    import msvcrt

    def get_key():
        if msvcrt.kbhit():
            return msvcrt.getch().decode("utf-8").lower()
        return None

else:  # Linux
    import termios, tty, select

    def get_key():
        dr, _, _ = select.select([sys.stdin], [], [], 0)
        if dr:
            return sys.stdin.read(1).lower()
        return None


class Cell:
    def __init__(self, alive=False):
        self.alive = alive

    def __repr__(self):
        return "◘" if self.alive else "♦"


class Universe:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.generate_random_grid()

    def generate_random_grid(self):
        self.grid = [
            [Cell(random.choice([True, False])) for _ in range(self.width)]
            for _ in range(self.height)
        ]

    def display(self, generation, pause=False):
        os.system("cls" if os.name == "nt" else "clear")
        print(f"Génération : {generation}\n")
        for row in self.grid:
            print(" ".join(str(cell) for cell in row))
        print()
        if pause:
            print()
        else:
            print("(Appuyez sur [Entrée] pour mettre en pause)")

    def count_neighbors(self, x, y):
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

    # Règle du jeu de la vie pour la génération suivante #
    def next_generation(self):
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


# --- Fonction demander_taille ---
def demander_taille():
    while True:
        try:
            width = int(input("Entrez la largeur de la grille (max 70) : "))
            height = int(input("Entrez la hauteur de la grille (max 70) : "))
            
            if 1 <= width <= 70 and 1 <= height <= 70:
                return width, height
            else:
                print("⚠️  Les dimensions doivent être comprises entre 1 et 100.\n")

        except ValueError:
            print("❌ Veuillez entrer un nombre entier valide.\n")