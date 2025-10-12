import random


def get_grid_size():
    while True:
        try:
            size = int(input("Taille de la grille (n×n) : "))
            if size > 0:
                return size
            print("La taille doit être positive.")
        except ValueError:
            print("Entrez un nombre entier.")


def generate_random_grid(size, density=0.3):
    return [[1 if random.random() < density else 0 for _ in range(size)] for _ in range(size)]


def generate_empty_grid(size):
    return [[0 for _ in range(size)] for _ in range(size)]


def display_grid(grid):
    if not grid:
        print("Grille vide")
        return
    
    size = len(grid)
    print(f"\nGrille {size}×{size}")
    print("-" * (size * 2 + 1))
    
    for row in grid:
        print("|", end="")
        for cell in row:
            symbol = "●" if cell == 1 else " "
            print(symbol, end="|")
        print()
    
    print("-" * (size * 2 + 1))
    
    total_cells = size * size
    living_cells = sum(sum(row) for row in grid)
    print(f"Cellules vivantes: {living_cells}/{total_cells}")


def create_grid():
    print("Génération de grille - Jeu de la Vie de Conway")
    
    size = get_grid_size()
    
    print(f"\nGrille {size}×{size}")
    print("1. Grille aléatoire")
    print("2. Grille vide")
    
    while True:
        choice = input("Choix (1 ou 2) : ").strip()
        
        if choice == "1":
            try:
                density = float(input("Densité (0.0-1.0, défaut 0.3) : ") or "0.3")
                if 0 <= density <= 1:
                    grid = generate_random_grid(size, density)
                    break
                else:
                    print("Densité entre 0.0 et 1.0")
            except ValueError:
                grid = generate_random_grid(size, 0.3)
                break
        
        elif choice == "2":
            grid = generate_empty_grid(size)
            break
        
        else:
            print("Tapez 1 ou 2")
    
    print("\nGrille générée !")
    display_grid(grid)
    
    return grid, size


if __name__ == "__main__":
    grid, size = create_grid()
