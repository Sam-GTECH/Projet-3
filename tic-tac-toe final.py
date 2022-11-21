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

#Crééer une fonction convertToGridIndex qui prend un argument x et qui renvoit la position de l'index x dans la grille
def convertToGridIndex(x:int)->tuple:
    #Si x est égal à 1
    if x == 1:
        # retourner le tuple (0, 0)
        return 0, 0
    #Sinon si x est égal à 2
    elif x == 2:
        # retourner le tuple (0, 1)
        return 0, 1
    #Sinon si x est égal à 3
    elif x == 3:
        # retourner le tuple (0, 2)
        return 0, 2
    #Sinon si x est égal à 4
    elif x == 4:
        # retourner le tuple (1, 0)
        return 1, 0
    #Sinon si x est égal à 5
    elif x == 5:
        # retourner le tuple (1, 1)
        return 1, 1
    #Sinon si x est égal à 6
    elif x == 6:
        # retourner le tuple (1, 2)
        return 1, 2
    #Sinon si x est égal à 7
    elif x == 7:
        # retourner le tuple (2, 0)
        return 2, 0
    #Sinon si x est égal à 8
    elif x == 8:
        # retourner le tuple (2, 1)
        return 2, 1
    #Sinon si x est égal à 9
    elif x == 9:
        # retourner le tuple (2, 2)
        return 2, 2
    # Elever une erreur de type IndexError
    raise IndexError

# définir une function convertToNormalIndex qui prend des arguments x et y et renvoit l'index de la position x et y dans la grille
def convertToNormalIndex(x:int, y:int)->int:
    #retourner le résultat de ((x*3)+y)+1
    return ((x*3)+y)+1

#Définir une fonction checkVictory qui vérifie si une ligne de l'argument nb a été formé
def checkVictory(nb:int)->bool:
    # Définir verif à 0
    verif = 0
    # Vertical lines
    # Faire une boucle qui parcoure grid en utilisant une variable x
    for x in grid:
        # Faire une boucle qui parcourt x en utilisant une variable y
        for y in x:
            # Si y est égal à nb
            if y==nb:
                #Ajouter 1 à verif
                verif=verif+1
                #Si verif est égal à 3
                if verif==3:
                    #Retourner True
                    return True
            # Sinon
            else:
                # Assigne 0 à verif
                verif = 0
                # Quitte la boucle
                break
    
    #Horrizontal lines
    # Faire une boucle qui se répète 3 fois en utilisant une valeur y
    for y in range(3):
        # Faire une boucle qui se répète 3 fois en utilisant une valeur x
        for x in range(3):
            # Si la valeur à la position x, y dans la grid est égal à nb
            if grid[x][y]==nb:
                #Ajouter 1 à verif
                verif=verif+1
                #Si verif est égal à 3
                if verif==3:
                    # Renvoie True
                    return True
            #Sinon
            else:
                # assigner verif à 0
                verif = 0
                # Quitter la boucle
                break
    
    #Diagonal lines
    #Si grid[0][0], grid[1][1] et grid[2][2] sont égal à nb ou que grid[2][0], grid[1][1], grid[0][2] sont égal à nb
    if (grid[0][0]==nb and grid[1][1]==nb and grid[2][2]==nb) or (grid[2][0]==nb and grid[1][1]==nb and grid[0][2]==nb):
        # Retourne True
        return True
    # Retourne False
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
        #mettre choix à une entrée input avec une phrase disant quel joueur doit jouer en concatenant 1 ou 2 suivant si playerisOne est True ou False
        choice = input("It's the Player "+ (playerisOne and "1" or "2") +"'s turn! (1-9) ")
        #essayer
        try:
            #convertir choice en integer
            choice = int(choice)
            #si choice est inférieur à 1 ou supérieur à 9:
            if choice<1 or choice>9:
                #Mettre choix à None
                choice = None
                #afficher un message d'erreur
                print("The user choice is out of range (must be between 1 and 9)")
            #Si la case choisie est prise
            if not checkGrid(choice):
                #Mettre choix à None
                choice = None
                #afficher un message disant que la case est prise
                print("The chosen case is already taken.")
        #si l'éssai échoue
        except:
            #Mettre choix à None
            choice = None
            #afficher "The user choice should be an integer"
            print("The user choice should be an integer")
    #assigner à des variable x et y la position de l'index choice dans la grille
    x, y = convertToGridIndex(choice)

    #assigner à la grid en position x, y 1 ou 2 suivant si playerisOne est True ou False
    grid[x][y] = playerisOne and 1 or 2
    #mettre choix à none
    choice = None
    #inverser la valeur booleenne de playerisOne
    playerisOne = not playerisOne
    #si checkVictory() renvoit True par le joueur 1:
    if checkVictory(1):
        #afficher un message de victoire pour le joueur 1
        print("\n\nThe Player 1 won!!")
        #quitter la boucle
        break
    #Sinon si checkVictory() renvoit True par le joueur 2:
    elif checkVictory(2):
        #afficher un message de victoire pour le joueur 2
        print("\n\nThe Player 2 won!")
        #quitter la boucle
        break
    #sinon isGridFull renvoit True
    elif isGridFull():
        #afficher un message annonçant l'égalité 
        print("Tie!")
        #quitter la boucle
        break
#afficher la grille
printGrid()

# END
