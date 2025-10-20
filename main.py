from game import Universe, demander_taille, get_key
import sys
import time
import os

if __name__ == "__main__":
    while True:
        width, height = demander_taille()
        universe = Universe(width, height)
        generation = 0
        paused = False

        while True:
            universe.display(generation, paused)
            key = get_key()

            # --- GESTION DES TOUCHES ---
            if key in ["\r", "\n"]:  # Entrée -> pause / reprise
                if not paused:
                    paused = True
                    print("\n⏸ Jeu en pause.")
                    print("👉 Appuyez sur [ENTRÉE] pour continuer.")
                    print("👉 Appuyez sur [n] pour une nouvelle partie.")
                    print("👉 Appuyez sur [q] pour quitter.\n")

                    # Boucle d’attente pendant la pause
                    while paused:
                        key = get_key()
                        if key in ["\r", "\n"]:
                            paused = False  # reprendre
                        elif key == "n":
                            os.system("cls" if os.name == "nt" else "clear")
                            break  # nouvelle partie
                        elif key == "q":
                            print("Fin du programme, à bientôt jeune padawan.")
                            sys.exit()
                        time.sleep(0.1)

                    if key == "n":  # si l'utilisateur veut une nouvelle partie
                        break

                else:
                    paused = False  # si déjà en pause, on reprend directement

            elif key == "n":
                break  
            elif key == "q":
                print("Fin du programme, à bientôt jeune padawan.")
                sys.exit()

            # --- AVANCE NORMAL DU JEU ---
            if not paused:
                time.sleep(1)
                generation += 1
                universe.next_generation()
