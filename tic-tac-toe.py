# DEBUT

# On importe la librarie random
import random

#On atttribue à une variable grid une matrix de 3 par 3
grid = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

# Attribue à la variable playerisOne la valeur True ou False en utilisant une condition avec random.randint(0, 1)
playerisOne = random.randint(0,1)==0

#Déclarer la variable choice sans valeur (None)
choice = None

#Définir printGrid qui affiche la grille du jeu
def printGrid():
    # Faire une boucle qui se répète suivant le nombre de lignes dans grid
    for i in range(len(grid)):
        #Si i est égal à zéro
        if i==0:
            #On affiche "┌─┬─┬─┐", le sommet de la grille
            print("┌─┬─┬─┐")
        #On affiche une barre de séparation
        print("│", end="")
        # Faire une boucle qui se répète suivant le nombre de collones dans grid
        for j in grid[i]:
            # Si j est égal à 0
            if j==0:
                #afficher un espace vide
                print(" ", end="")
            # Sinon si j est égal à 1
            elif j==1:
                #Afficher un O
                print("O", end="")
            # Sinon si j est égal à 2
            elif j==2:
                # Afficher un X
                print("X", end="")
            #On affiche une barre de séparation
            print("│", end="")
        #Si i est égal à 2
        if i==2:
            #Affichier "\n└─┴─┴─┘", le  bas de la grille
            print("\n└─┴─┴─┘")
        #Sinon
        else:
            #On affiche "\n├─┼─┼─┤" qui sépare deux lignes
            print("\n├─┼─┼─┤")

#Faire une fonction checkGrid qui prend une position x obligatoire et une position y optionnel. Si y n'est pas renseigné, la valeur par défaut est -1
def checkGrid(x:int, y:int=-1)->bool:
    # Si y est égal à -1
    if y==-1:
        #On appelle convertToGridIndex avec x comme argument et on donne les valeurs renvoyés aux variables x et y
        x, y = convertToGridIndex(x)

    #On retourne si la valeur de la grid aux positions x et y est égal à 0
    return grid[x][y]==0


def convertToGridIndex(x:int)->tuple:
    if x == 1:
        return 0, 0
    elif x == 2:
        return 0, 1
    elif x == 3:
        return 0, 2
    elif x == 4:
        return 1, 0
    elif x == 5:
        return 1, 1
    elif x == 6:
        return 1, 2
    elif x == 7:
        return 2, 0
    elif x == 8:
        return 2, 1
    elif x == 9:
        return 2, 2
    raise IndexError

def convertToNormalIndex(x:int, y:int)->int:
    return ((x*3)+y)+1

def checkVictory(nb:int)->bool:
    verif = 0
    # Vertical lines
    for x in grid:
        for y in x:
            if y==nb:
                verif=verif+1
                if verif==3:
                    return True
            else:
                verif = 0
                break
    
    #Horrizental lines
    for y in range(3):
        for x in range(3):
            if grid[x][y]==nb:
                verif=verif+1
                if verif==3:
                    return True
            else:
                verif = 0
                break
    
    #Diagonal lines
    if (grid[0][0]==nb and grid[1][1]==nb and grid[2][2]==nb) or (grid[2][0]==nb and grid[1][1]==nb and grid[0][2]==nb):
        return True
    return False
#definir une fonction renvoie la valeur a la position de la grille
def getBoxValue(i):
    #convertir i en x, y
    x, y = convertToGridIndex(i)
    #retourner la valeur de la position x, y dans la grille
    return grid[x][y]

#définir une fonction permettant de détecter si la grille est pleine
def isGridFull():
    #définir une variable boxTaken
    boxTaken = 0
    #Pour x dans une rangée de  3
    for x in range(3):
        #Pour y dans une rangée de 3
        for y in range(3):
            #Si grille x, y ne vaut pas 0
            if grid[x][y]!=0:
                #ajouter 1 a boxTaken
                boxTaken += 1
    #retourner boxTaken == 9 (true ou false)
    return boxTaken==9

#boucle infinie
while True:
    #Tant que choice est égal à none
    while choice==None:
        #afficher la grille
        printGrid()
        #mettre choix à une entrée input avec une phrase disant quel joueur doit jouer
        choice = input("It's the Player "+ (playerisOne and "1" or "2") +"'s turn! (1-9) ")
        #essayer
        try:
            #convertir choice en integer
            choice = int(choice)
            #si choice <1 ou > 9:
            if choice<1 or choice>9:
                #afficher un message d'erreur
                raise IndexError
            #Si la case choisie est prise
            if not checkGrid(choice):
                #Mettre choix à None
                choice = None
                #afficher un message disant que la case est prise
                print("The chosen case is already taken.")
        #si l'éssai échoue
        except:
            #afficher "The user choice should be an integer"
            raise TypeError("The user choice should be an integer")
    #définir des variable x et y de position dans la grille
    x, y = convertToGridIndex(choice)

    #défir grille x, y selon quel joueur joue
    grid[x][y] = playerisOne and 1 or 2
    #mettre choix à none
    choice = None
    #inverser la valeur booleenne de playerisOne
    playerisOne = not playerisOne
    #si une victoire est vérifié par le joueur 1:
    if checkVictory(1):
        #afficher un message de victoire pour le joueur 1
        print("\n\nThe Player 1 won!!")
        #quitter la boucle
        break
    #Sinon si une victoire est vérifié par le joueur 2:
    elif checkVictory(2):
        #afficher un message de victoire pour le joueur 2
        print("\n\nThe Player 2 won!")
        #quitter la boucle
        break
    #sinon si la grille est pleine:
    elif isGridFull():
        #afficher un message 
        print("Tie!")
        #quitter la boucle
        break
#afficher la grille
printGrid()

# END