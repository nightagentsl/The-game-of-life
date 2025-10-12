from grid_generation import create_grid, display_grid


class ConwayGame:
    def __init__(self):
        self.grid = None
        self.size = 0
        self.generation = 0
    
    def initialize_game(self):
        print("Initialisation du Jeu de la Vie de Conway")
        self.grid, self.size = create_grid()
        self.generation = 0
    
    def display_current_state(self):
        print(f"\nGénération {self.generation}")
        display_grid(self.grid)
    
    def count_living_neighbors(self, row, col):
        count = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = row + dr, col + dc
                if 0 <= nr < self.size and 0 <= nc < self.size:
                    count += self.grid[nr][nc]
        return count
    
    def evolve_grid(self):
        if not self.grid:
            print("Aucune grille initialisée")
            return
        
        new_grid = []
        for row in range(self.size):
            new_row = []
            for col in range(self.size):
                neighbors = self.count_living_neighbors(row, col)
                current_cell = self.grid[row][col]
                
                if neighbors == 3:
                    new_cell = 1
                elif neighbors == 2:
                    new_cell = current_cell
                else:
                    new_cell = 0
                
                new_row.append(new_cell)
            new_grid.append(new_row)
        
        self.grid = new_grid
        self.generation += 1
    
    def run_simulation(self, max_generations=10):
        if not self.grid:
            print("Veuillez d'abord initialiser une grille")
            return
        
        print(f"Simulation pour {max_generations} générations")
        
        for gen in range(max_generations):
            self.display_current_state()
            if gen < max_generations - 1:
                input("\nEntrée pour la génération suivante...")
                self.evolve_grid()
        
        print("\nSimulation terminée!")
    
    def run_interactive(self):
        if not self.grid:
            print("Veuillez d'abord initialiser une grille")
            return
        
        while True:
            self.display_current_state()
            
            print("\n1. Génération suivante")
            print("2. Nouvelle grille")
            print("3. Quitter")
            
            choice = input("Choix : ").strip()
            
            if choice == "1":
                self.evolve_grid()
            elif choice == "2":
                self.initialize_game()
            elif choice == "3":
                break
            else:
                print("Choix invalide")


def main():
    game = ConwayGame()
    
    print("Jeu de la Vie de Conway")
    print("Partie 1: Génération de grille (implémentée)")
    print("Partie 2: Évolution de grille (implémentée)")
    
    while True:
        print("\n1. Créer une grille")
        print("2. Simulation automatique")
        print("3. Mode interactif")
        print("4. Quitter")
        
        choice = input("Choix : ").strip()
        
        if choice == "1":
            game.initialize_game()
        elif choice == "2":
            if game.grid:
                generations = int(input("Nombre de générations (défaut 5) : ") or "5")
                game.run_simulation(generations)
            else:
                print("Créez d'abord une grille")
        elif choice == "3":
            if game.grid:
                game.run_interactive()
            else:
                print("Créez d'abord une grille")
        elif choice == "4":
            break
        else:
            print("Choix invalide")


if __name__ == "__main__":
    main()
