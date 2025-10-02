import pygame, sys
from pygame.locals import *
import random

# Classe qui représente une cellule individuelle de la grille
class Cell:

    def __init__(self):
        self.life = False          # Etat de la cellule (vivante = True, morte = False)
        self.neighbours = 0        # Nombre de voisins vivants autour

    # Définit le nombre de voisins
    def setNeighbours(self, n):
        self.neighbours = n

    # Renvoie le nombre de voisins
    def getNeighbours(self):
        return self.neighbours

    # Renvoie True si la cellule est vivante
    def getLife(self):
        return self.life

    # Rend la cellule vivante
    def setAlive(self):
        self.life = True

    # Rend la cellule morte
    def setDead(self):
        self.life = False


# Classe qui représente l’univers (la grille complète du jeu)
class Universe:

    def __init__(self, height, width):
        self.height = int(height)   # hauteur de la grille (nb de cellules verticalement)
        self.width = int(width)     # largeur de la grille (nb de cellules horizontalement)

        # Création d’une grille de cellules (tableau 2D de Cell())
        self.universe = [[Cell() for i in range(self.height)] for j in range(self.width)]

    # Retourne une cellule spécifique (coordonnées x, y)
    def getCell(self, x, y):
        return self.universe[x][y]

    # Remplit la grille de manière aléatoire (vivante ou morte)
    def randomize(self):
        for x in range(self.width):
            for y in range(self.height):
                if random.randint(0, 1) == 1:   # 50% de chance d’être vivante
                    self.setAlive(x, y)

    # Dessine la grille complète avec pygame
    def drawGrid(self):
        # Pour chaque cellule de la grille
        for x in range(self.width): 
            for y in range(self.height): 
                if self.getCell(x, y).getLife():   # Si vivante → rectangle vert
                    pygame.draw.rect(DISPLAYSURF, GREEN, (x * CELLSIZE, y * CELLSIZE, CELLSIZE, CELLSIZE))
                else:                              # Si morte → rectangle blanc
                    pygame.draw.rect(DISPLAYSURF, WHITE, (x * CELLSIZE, y * CELLSIZE, CELLSIZE, CELLSIZE))

    # Compte le nombre de voisins vivants autour de la cellule (i, j)
    def countNeighbours(self, i , j):
        neighbours = 0
        for x in range(i-1, i+2):      # Parcourt les 3 lignes autour de i
            for y in range(j-1, j+2):  # Parcourt les 3 colonnes autour de j
                if self.getLife(x, y) and (x!=i or y!=j):  # On ignore la cellule elle-même
                    neighbours += 1
        self.setNeighbours(i, j, neighbours)

    # Fait évoluer tout l’univers d’une génération (un "tick")
    def tick(self):
        # 1. Calcul du nombre de voisins pour chaque cellule
        for x in range(self.width): 
            for y in range(self.height): 
                self.getCell(x, y).setNeighbours(self.countNeighbours(x, y))

        # 2. Application des règles de Conway à chaque cellule
        for x in range(self.width): 
            for y in range(self.height):
                n = self.getNeighbours(x, y)  # Récupère nb voisins
                if n == None:
                    n = 0

                # Règles du jeu :
                if n < 2 or n > 3:       # <2 solitude, >3 surpopulation
                    self.setDead(x, y)
                else:                    # 2 ou 3 voisins = survie ou naissance
                    self.setAlive(x, y)     

    # Met à jour le nombre de voisins pour une cellule donnée
    def setNeighbours(self, x, y, n):
        if x <= self.width and y <= self.height:
            self.getCell(x, y).setNeighbours(n)
        else:
            print("ERROR = out of scope parameters for setNeighbours")

    # Récupère le nombre de voisins pour une cellule
    def getNeighbours(self, x, y):
        if x <= self.width and y <= self.height:
            return self.getCell(x, y).getNeighbours()
        else:
            return 0

    # Rend une cellule vivante
    def setAlive(self, x, y):
        if x <= self.width and y <= self.height:
            self.getCell(x, y).setAlive()
            self.getCell(x, y).setNeighbours(0)  # réinitialise ses voisins
        else:
            print("ERROR = out of scope parameters for setAlive")

    # Rend une cellule morte
    def setDead(self, x, y):
        if x <= self.width and y <= self.height:
            self.getCell(x, y).setDead()
            self.getCell(x, y).setNeighbours(0)
        else:
            print("ERROR = out of scope parameters for setDead")

    # Vérifie si une cellule est vivante (et gère les bords de la grille)
    def getLife(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False   # Hors de la grille → considéré comme mort
        else:
            return self.getCell(x, y).getLife()


# Paramètres de la fenêtre et des cellules
WINDOWWIDTH = 800
WINDOWHEIGHT = 400
CELLSIZE = 10

# Vérifie que la grille correspond bien à la taille des cellules
assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size"
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size"
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)   # nombre de cellules en largeur
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE) # nombre de cellules en hauteur

# Couleurs utilisées
BLACK =    (0,  0,  0)
WHITE =    (255,255,255)
DARKGRAY = (40, 40, 40)
GREEN =    (0,  255,0)


def main():
    pygame.init()

    # Création de la fenêtre pygame
    global DISPLAYSURF
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    DISPLAYSURF.fill(WHITE) # Remplit l’écran en blanc

    pygame.display.set_caption('Game of Life')

    # Création de l’univers (grille de cellules)
    game = Universe(CELLHEIGHT, CELLWIDTH)

    # Remplissage aléatoire de départ
    game.randomize()

    # Exemple : forcer trois cellules vivantes alignées
    game.setAlive(10, 10)
    game.setAlive(11, 10)
    game.setAlive(12, 10)

    # Dessine la grille initiale
    game.drawGrid()
    pygame.display.update()

    # Boucle principale du programme
    while True: 
        for event in pygame.event.get():
            if event.type == QUIT:   # Si l’utilisateur ferme la fenêtre
                pygame.quit()
                sys.exit()

        # Ici on pourrait activer l’évolution automatique :
        # game.tick()
        # game.drawGrid()

        pygame.display.update()


main()

if __name__=='__main__':
    main()
