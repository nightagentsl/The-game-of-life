from grid_generation import generate_random_grid, generate_empty_grid, display_grid


def test_grid_creation():
    print("Test de création de grilles")
    
    empty_grid = generate_empty_grid(3)
    print("Grille vide 3×3:")
    display_grid(empty_grid)
    
    random_grid = generate_random_grid(3, 0.5)
    print("\nGrille aléatoire 3×3 (densité 0.5):")
    display_grid(random_grid)
    
    print("\nTests terminés avec succès !")


if __name__ == "__main__":
    test_grid_creation()
