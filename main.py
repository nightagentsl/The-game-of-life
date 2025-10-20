from game import Universe, ask_dimension, get_key, save_grid, charge_last_grid
import sys
import time
import os

if __name__ == "__main__":
    while True:
        print(" Conways Game of life")
        choix = input("Do you want to load last save ? (o/n) : ").lower()

        if choix == "o":
            universe, generation = charge_last_grid()
            if universe is None:
                width, height = ask_dimension()
                universe = Universe(width, height)
                generation = 0
        else:
            width, height = ask_dimension()
            universe = Universe(width, height)
            generation = 0

        
        paused = False

        while True:
            universe.display(generation, paused)
            key = get_key()

            # key Imputs
            if key in ["\r", "\n"]:  # enter → pause or resume
                if not paused:
                    paused = True
                    print("\n⏸ Jeu en pause.")
                    print("👉 Appuyez sur [ENTRÉE] pour continuer.")
                    print("👉 Appuyez sur [n] pour une nouvelle partie.")
                    print("👉 Appuyez sur [q] pour quitter.\n")

                    # loop waiting in pause
                    while paused:
                        key = get_key()
                        if key in ["\r", "\n"]:
                            paused = False  # resume
                        elif key == "n":
                            os.system("cls" if os.name == "nt" else "clear")
                            save_grid(universe, generation)
                            break  # new game
                        elif key == "q":
                            print("End of the program, see you soon young padawan.")
                            save_grid(universe, generation)
                            sys.exit()
                        time.sleep(0.1)

                    if key == "n":  # if user wants a new game
                        save_grid(universe, generation)
                        break

                else:
                    paused = False  # if in pause, continue the game

            elif key == "n":
                save_grid(universe, generation)
                break  
            elif key == "q":
                save_grid(universe, generation)
                print("End of the program, see you soon young padawan.")
                sys.exit()

            # game logic
            if not paused:
                time.sleep(1)
                generation += 1
                universe.next_generation()
