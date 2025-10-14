# The-game-of-life
TP final en python - Jeu de la Vie de Conway

## ⚠️ Structure du projet
**IMPORTANT :** Tous les fichiers Python sont dans le dossier `grid_generation/`  
**Ne pas créer de fichiers .py dans le dossier racine !**

## 📋 Contexte du TP

Le jeu de la Vie de Conway est un « jeu à zéro joueur ». Le jeu se déroule sur une grille n×n où chaque cellule est soit vivante (1), soit morte (0) et possède 8 voisines.

### Règles d'évolution
À chaque tour :
- **3 voisines vivantes** → la cellule devient vivante
- **2 voisines vivantes** → la cellule garde son état (vivant reste vivant, mort reste mort)
- **Autrement** → la cellule meurt

## ✅ Partie 1 : Génération de grille (Implémentée)

### Ce qui a été fait
- **`grid_generation.py`** : Module principal avec toutes les fonctions
- **`simple_grid.py`** : Version simplifiée pour tests rapides
- **`conway_interface.py`** : Interface facile à utiliser

### Fonctions disponibles pour ton travail

#### Utilisation simple
```python
from grid_generation.grid_generation import create_grid, display_grid

# Générer une grille initiale
grille, taille = create_grid()
# L'utilisateur choisit la taille et le type de grille

# Afficher la grille
display_grid(grille)
```

### 🧪 Commandes pour tester la grille

#### Tests rapides
```bash
# Test simple et rapide
python grid_generation/simple_grid.py

# Test complet avec options
python grid_generation/grid_generation.py

# Tests automatisés
python grid_generation/test_grid.py

# Interface complète
python grid_generation/conway_interface.py
```

#### Tests personnalisés
```bash
# Grille aléatoire 5×5
python -c "from grid_generation.grid_generation import *; display_grid(generate_random_grid(5, 0.3))"

# Grille vide 3×3
python -c "from grid_generation.grid_generation import *; display_grid(generate_empty_grid(3))"

# Test avec différentes densités
python -c "
from grid_generation.grid_generation import *
for d in [0.1, 0.3, 0.5, 0.7]:
    print(f'Densité {d}:')
    display_grid(generate_random_grid(4, d))
"
```

#### Format de la grille
```python
# Exemple grille 3x3
grille = [
    [0, 1, 0],  # 0 = mort, 1 = vivant
    [1, 1, 1],
    [0, 0, 0]
]
```

## 🔄 Partie 2 : Évolution de la grille (À faire - Titi)

### Ce que tu dois implémenter

#### 1. Fonction pour compter les voisins
```python
def compter_voisins(grille, ligne, colonne):
    """
    Compte les voisins vivants d'une cellule
    Attention aux bords de la grille !
    """
    # À implémenter
    pass
```

#### 2. Fonction d'évolution
```python
def evoluer_grille(grille):
    """
    Calcule la génération suivante selon les règles de Conway
    Retourne une nouvelle grille
    """
    # À implémenter
    pass
```

#### 3. Boucle principale du jeu
```python
from grid_generation.grid_generation import create_grid, display_grid

# Grille initiale
grille, taille = create_grid()

# Boucle du jeu
while True:
    display_grid(grille)
    grille = evoluer_grille(grille)  # Nouvelle génération
    input("Entrée pour continuer...")
```

### Points importants
- ⚠️ **Attention aux bords** : Les cellules sur les bords ont moins de 8 voisins
- ⚠️ **Calcul simultané** : Toutes les cellules évoluent en même temps (utilise une nouvelle grille)
- 🎯 **Les 8 voisins** : diagonales comprises (haut, bas, gauche, droite + 4 diagonales)