# DEBUT

# On importe la librarie random
import random

#On atttribue à une variable grid une matrix de 3 par 3
grid = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

# Attribue à la variable playerTurn la valeur False
playerTurn = False

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
        if i==2:
            print("\n└─┴─┴─┘")
        else:
            print("\n├─┼─┼─┤")

def checkGrid(x:int, y:int=-1)->bool:
    if y==-1:
        x, y = convertToGridIndex(x)

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

def getBoxValue(i):
    x, y = convertToGridIndex(i)
    return grid[x][y]


def ordiChoice():
    rand = random.randint(1, 9)
    while not checkGrid(*convertToGridIndex(rand)):
        rand = random.randint(1, 9)
    return rand
                
def isGridFull():
    boxTaken = 0
    for x in range(3):
        for y in range(3):
            if grid[x][y]!=0:
                boxTaken += 1
    return boxTaken==9


while True:
    if playerTurn:
        while choice==None:
            printGrid()
            choice = input("It's your turn! (1-9) ")
            try:
                choice = int(choice)
                if choice<1 or choice>9:
                    raise IndexError
                if not checkGrid(choice):
                    choice = None
                    print("The chosen case is already taken.")
            except:
                raise TypeError("The user choice should be an integer")
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

# END