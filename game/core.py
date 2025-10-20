import random
import os
import sys
import json

# Detect key imputs
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
            print("Press [ENTER] to pause, [n] for new game, [q] to quit.")

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

    # Conway game of life rule for the next generation #
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


# ask heght and width from user #
def ask_dimension():
    while True:
        try:
            width = int(input("Enter the henght of the grid (max 70) : "))
            height = int(input("enter the width of the grid (max 70) : "))
            
            if 1 <= width <= 70 and 1 <= height <= 70:
                return width, height
            else:
                print("⚠️  Dimension need to be between 1 et 100.\n")

        except ValueError:
            print("❌ Please enter a valid number.\n")
            
def save_grid(universe, generation):
    # Save the current generation in an JSON file. #
    data = {
        "generation": generation,
        "width": universe.width,
        "height": universe.height,
        "grid": [[cell.alive for cell in row] for row in universe.grid],
    }
    with open("save.txt", "w") as f:
        json.dump(data, f)
    print("Grid saved successfully !")

def charge_last_grid():
    # Charge the last game grid #
    try:
        with open("save.txt", "r") as f:
            data = json.load(f)

        u = Universe(data["width"], data["height"])
        for x in range(u.height):
            for y in range(u.width):
                u.grid[x][y].alive = data["grid"][x][y]
        print("Save charge successfully !\n")
        return u, data["generation"]
    except FileNotFoundError:
        print("No save was found.\n")
        return None, 0            