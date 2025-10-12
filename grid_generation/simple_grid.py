import random


def demander_taille_grille():
    return int(input("Taille de la grille (ex: 5 pour 5×5) : "))


def creer_grille_aleatoire(taille):
    return [[1 if random.random() < 0.3 else 0 for _ in range(taille)] for _ in range(taille)]


def afficher_grille(grille):
    print("\nGrille :")
    for ligne in grille:
        for cellule in ligne:
            print("●" if cellule == 1 else "○", end=" ")
        print()


if __name__ == "__main__":
    print("Génération de grille - Jeu de la Vie")
    
    taille = demander_taille_grille()
    ma_grille = creer_grille_aleatoire(taille)
    afficher_grille(ma_grille)
    
    print(f"\nGrille {taille}×{taille} créée ! (0=mort, 1=vivant)")
