# DEBUT

# On importe la librarie random
import random

#On atttribue à une variable grid une matrix de 3 par 3
grid = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

# Attribue à la variable playerisOne la valeur True ou False en utilisant une condition avec random.randint(0, 1)
playerTurn = random.randint(0,1)==0

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

#Créer une fonction convertToGridIndex qui prend un argument x et qui renvoit la position de l'index x dans la grille
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


def ordiChoice():
    corners = [1, 3, 7, 9]
    random.shuffle(corners)

    ligne = 0
    possibleLastBox = None

    winBox = None
    blockBox = None

    # First diagonal line
    for i in [1, 5, 9]:
        x, y = convertToGridIndex(i)
        if grid[x][y]==1:
            ligne=ligne+1
        elif grid[x][y]==2:
            ligne=ligne-1
        else:
            if possibleLastBox!=None:
                break
            #if grid[x][y]!=2:
            possibleLastBox = i
    if ligne == 2 and possibleLastBox and getBoxValue(possibleLastBox)==0:
        blockBox = possibleLastBox
        ligne = 0
        possibleLastBox = None
    elif ligne == -2 and possibleLastBox and getBoxValue(possibleLastBox)==0:
        winBox = possibleLastBox
        ligne = 0
        possibleLastBox = None
    else:
        ligne = 0
        possibleLastBox = None

    # Second diagonal line
    for i in [3, 5, 7]:
        x, y = convertToGridIndex(i)
        if grid[x][y]==1:
            ligne=ligne+1
        elif grid[x][y]==2:
            ligne=ligne-1
        else:
            if possibleLastBox!=None:
                break
            #if grid[x][y]!=2:
            possibleLastBox = i
    if ligne == 2 and possibleLastBox and getBoxValue(possibleLastBox)==0:
        blockBox = possibleLastBox
        ligne = 0
        possibleLastBox = None
    elif ligne == -2 and possibleLastBox and getBoxValue(possibleLastBox)==0:
        winBox = possibleLastBox
        ligne = 0
        possibleLastBox = None
    else:
        ligne = 0
        possibleLastBox = None

    for x in range(3):
        for y in range(3):
            if grid[x][y]==1:
                ligne=ligne+1
            elif grid[x][y]==2:
                ligne=ligne-1
            else:
                if possibleLastBox!=None:
                    break
                #if grid[x][y]!=2:
                possibleLastBox = convertToNormalIndex(x, y)
        if ligne == 2 and possibleLastBox and getBoxValue(possibleLastBox)==0:
            blockBox = possibleLastBox
            ligne = 0
            possibleLastBox = None
        elif ligne == -2 and possibleLastBox and getBoxValue(possibleLastBox)==0:
            winBox = possibleLastBox
            ligne = 0
            possibleLastBox = None
        else:
            ligne = 0
            possibleLastBox = None

    # Créer une boucle de rangée 0 à 2 avec un index y
    for y in range(3):
        # Créer une boucle de rangée 0 à 2 avec un index x
        for x in range(3):
            # Si la position x, y dans la grille est égal à 1
            if grid[x][y]==1:
                # Ajouter 1 à ligne
                ligne=ligne+1
            # Sinon si la position x, y dans la grille est égal à 2
            elif grid[x][y]==2:
                # Diminuer ligne de 1
                ligne=ligne-1
            # Sinon
            else:
                # Si possible n'est pas None
                if possibleLastBox!=None:
                    # On sort de la boucle
                    break
                # Assigner ce que retourne convertToNormalIndex(x, y) à possibleLastBox
                possibleLastBox = convertToNormalIndex(x, y)
        # Si ligne est égale à 2 et que possibleLastBox existe et que la valeur que renvoit getBoxValeur(possibleLastBox) est égal à 0
        if ligne == 2 and possibleLastBox and getBoxValue(possibleLastBox)==0:
            # Assigner la valeur de possibleLastBox à blockBox
            blockBox = possibleLastBox
            # Assigner 0 à ligne
            ligne = 0
            # Assigner None à possibleLastBox
            possibleLastBox = None
        # Si ligne est égale à -2 et que possibleLastBox existe et que la valeur que renvoit getBoxValeur(possibleLastBox) est égal à 0
        elif ligne == -2 and possibleLastBox and getBoxValue(possibleLastBox)==0:
            # Assigner la valeur de possibleLastBox à winBox
            winBox = possibleLastBox
            # Assigner 0 à ligne
            ligne = 0
            # Assigner None à possibleLastBox
            possibleLastBox = None
        else:
            # Assigner 0 à ligne
            ligne = 0
            # Assigner None à possibleLastBox
            possibleLastBox = None

    # Si la valeur renvoyé par getBoxValue(5) est égal à 0
    if getBoxValue(5)==0:
        # Retourner 5
        return 5

    # Si winBox a une valeur attitrée
    if winBox:
        # Retourner winBox
        return winBox
    # Si blockBox a une valeur attitrée
    elif blockBox:
        # Retourner blockBox
        return blockBox

    # Créer une boucle qui itérère avec la valeur i dans la table corners
    for i in corners:
        # Si la valeur renvoyé par getBoxValue(i) est égal à 0
        if getBoxValue(i)==0:
            # Retourner i
            return i

    # Retourner un nombre aléatoire entre 1 et 9
    return random.randint(1, 9)

def isGridFull():
    boxTaken = 0
    for x in range(3):
        for y in range(3):
            if grid[x][y]!=0:
                boxTaken += 1
    return boxTaken==9

print("User: O | CPU: X")
while True:
    if playerTurn:
        while choice==None:
            printGrid()
            choice = input("It's your turn! (1-9) ")
            try:
                choice = int(choice)
                if choice<1 or choice>9:
                    choice = None
                    print("The user choice is out of range (must be between 1 and 9)")
                if not checkGrid(choice):
                    choice = None
                    print("The chosen case is already taken.")
            except:
                choice = None
                print("The user choice should be an integer")
    else:
        print("It's the ordi's turn!")
        while choice==None or not checkGrid(choice):
            choice = ordiChoice()
    x, y = convertToGridIndex(choice)

    grid[x][y] = playerTurn and 1 or 2
    choice = None
    playerTurn = not playerTurn

    if checkVictory(1):
        print("\n\nThe user won!!")
        break
    elif checkVictory(2):
        print("\n\nThe ordi won!")
        break
    elif isGridFull():
        print("Tie!")
        break
printGrid()