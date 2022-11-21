import random

grid = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

playerTurn = random.randint(0,1)==0

choice = None


def printGrid():
    for i in range(len(grid)):
        if i==0:
            print("┌─┬─┬─┐")
        print("│", end="")
        for j in grid[i]:
            if j==0:
                print(" ", end="")
            elif j==1:
                print("O", end="")
            elif j==2:
                print("X", end="")
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

#définir une fonction ordiChoice qui permettra à l'IA de faire des choix
def ordiChoice():
    #définition d'un tableau corner possédant les coins de la grille
    corners = [1, 3, 7, 9]
    #mélange les nombres dans la liste
    random.shuffle(corners)
    #définir ligne à 0
    ligne = 0
    #définir possibleLastBox à 0
    possibleLastBox = None
    #définir une variable winBox à None
    winBox = None
    #définir une variable blockBox à None
    blockBox = None
    
    #First diagonal line
    #faire une boucle dans la diagonal du coin supérieur gauche au coin inférieur droit:
    for i in [1, 5, 9]:
        #convertir l'index i en position x, y
        x, y = convertToGridIndex(i)
        #Si grille x, y vaut 1
        if grid[x][y]==1:
            #incrémenter ligne de 1
            ligne=ligne+1
        #Sinon si grille x, y vaut 2:
        elif grid[x][y]==2:
            #décrementer ligne de 1
            ligne=ligne-1
        #Sinon
        else:
            #Si possibleLastBox ne vaut pas None
            if possibleLastBox!=None:
                #quitter la boucle
                break
            #mettre possibleLastBox à i
            possibleLastBox = i
    #Si ligne vaut 2 et possibleLasteBox existe et que la valeur que renvoie getBoxValue(possibleLastBox) vaut 0:
    if ligne == 2 and possibleLastBox and getBoxValue(possibleLastBox)==0:
        #mettre blockBox à possibleLastBox
        blockBox = possibleLastBox
        #mettre ligne à 0
        ligne = 0
        #mettre possibleLastBox à None
        possibleLastBox = None
    #Sionon si ligne vaut -2 et possibleLasteBox existe et que la valeur que renvoie getBoxValue(possibleLastBox) vaut 0:
    elif ligne == -2 and possibleLastBox and getBoxValue(possibleLastBox)==0:
        #mettre winBox à possibleLastBox
        winBox = possibleLastBox
        #mettre ligne à 0
        ligne = 0
        #mettre possibleLastBox à None
        possibleLastBox = None
    #Sinon:
    else:
        #mettre ligne à 0
        ligne = 0
        #mettre possibleLastBox à 0
        possibleLastBox = None

    #Second diagonal line
    #faire une boucle dans la diagonal du coin supérieur droit au coin inférieur gauche:
    for i in [3, 5, 7]:
        #convertir l'index i en position x, y
        x, y = convertToGridIndex(i)
        #Si grille x, y vaut 1:
        if grid[x][y]==1:
            #incrémenter ligne de 1
            ligne=ligne+1
        #Sinon si grille x, y vaut 2:
        elif grid[x][y]==2:
            #décrementer ligne de 1
            ligne=ligne-1
        #Sinon
        else:
            #Si possibleLastBox ne vaut pas None:
            if possibleLastBox!=None:
                #quitter la boucle
                break
            #mettre possibleLastBox à i
            possibleLastBox = i
    #Si ligne vaut 2 et possibleLasteBox existe et que la valeur que renvoie getBoxValue(possibleLastBox) vaut 0:
    if ligne == 2 and possibleLastBox and getBoxValue(possibleLastBox)==0:
        #mettre blockBox à possibleLastBox
        blockBox = possibleLastBox
        #mettre ligne à 0
        ligne = 0
        #mettre possibleLastBox à None
        possibleLastBox = None
    #Sinon si ligne vaut -2 et possibleLasteBox existe et que la valeur que renvoie getBoxValue(possibleLastBox) vaut 0:
    elif ligne == -2 and possibleLastBox and getBoxValue(possibleLastBox)==0:
        #mettre winBox à possibleLastBox
        winBox = possibleLastBox
        #mettre ligne à 0
        ligne = 0
        #mettre possibleLastBox à None
        possibleLastBox = None
    #Sinon:
    else:
        #mettre ligne à 0
        ligne = 0
        #mettre possibleLastBox à None
        possibleLastBox = None
    #créer une boucle de rangée 0 à 2 avec un index x
    for x in range(3):
        #créer une boucle de rangée 0 à 2 avec un index y
        for y in range(3):
            #Si la position x, y dans la grille vaut 1:
            if grid[x][y]==1:
                #incrementer ligne de 1
                ligne=ligne+1
            #Sinon si la position x, y dans la grille vaut 2:
            elif grid[x][y]==2:
                #décrementer ligne de 1
                ligne=ligne-1
            #Sinon:
            else:
                #si possibleLastBox ne vaut pas None
                if possibleLastBox!=None:
                    #quitter la boucle
                    break
                #assigner ce que retourne convertToNormalIndex à possibleLastBox
                possibleLastBox = convertToNormalIndex(x, y)
        #Si ligne vaut 2 et possibleLasteBox existe et que la valeur que renvoie getBoxValue(possibleLastBox) vaut 0:
        if ligne == 2 and possibleLastBox and getBoxValue(possibleLastBox)==0:
            #mettre blockBox à possibleLastBox
            blockBox = possibleLastBox
            #mettre ligne à 0
            ligne = 0
            #mettre possibleLastBox à None
            possibleLastBox = None
        #Sinon si ligne vaut -2 et possibleLasteBox existe et que la valeur que renvoie getBoxValue(possibleLastBox) vaut 0:
        elif ligne == -2 and possibleLastBox and getBoxValue(possibleLastBox)==0:
            #mettre winBox à possibleLastBox
            winBox = possibleLastBox
            #mettre ligne à 0
            ligne = 0
            #mettre possibleLastBox à 0
            possibleLastBox = None
        #Sinon:
        else:
            #mettre ligne à 0
            ligne = 0
            #mettre possibleLastBox à None
            possibleLastBox = None

    for y in range(3):
        for x in range(3):
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

    if getBoxValue(5)==0:
        return 5

    if winBox:
        return winBox
    elif blockBox:
        return blockBox

    for i in corners:
        if getBoxValue(i)==0:
            return i
    return random.randint(1, 9)

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
#afficher un message montrant que l'utilisateur possède les O et l'ordi les X
print("User: O | CPU: X")
#boucle infinie
while True:
    #Si playerTurn vaut true:
    if playerTurn:
        #Tant qu'il n'y à pas de choix:
        while choice==None:
            #afficher la grille
            printGrid()
            #définir choix à une entrée utilisateur
            choice = input("It's your turn! (1-9) ")
            #essayer de:
            try:
                #convertir choice en entier
                choice = int(choice)
                #Si choice est inferieur à 1 ou supérieur à 9:
                if choice<1 or choice>9:
                    #mettre choix à None
                    choice = None
                    #afficher un message disant qu'il faut un nombre entre 1 et 9
                    print("The user choice is out of range (must be between 1 and 9)")
                #Si la case choisie est prise
                if not checkGrid(choice):
                    #mettre choix à None
                    choice = None
                    #afficher un message disant que la case est occupée
                    print("The chosen case is already taken.")
            #si l'essai echoue:
            except:
                #mettre choix à None
                choice = None
                #afficher un message disant que la réponse doit être un entier
                print("The user choice should be an integer")
    #Sinon:
    else:
        #afficher un message disant que l'IA doit jouer
        print("It's the ordi's turn!")
        #Tant que choice vaut None ou que la case choisie est prise
        while choice==None or not checkGrid(choice):
            #assigner ce que retourne ordiChoice à choice
            choice = ordiChoice()
    #assigner à x, y ce que retourne convertToGridIndex(choice)
    x, y = convertToGridIndex(choice)
    #assigner à la grid en position x, y 1 ou 2 suivant si playerTurn est True ou False
    grid[x][y] = playerTurn and 1 or 2
    #mettre choice à None
    choice = None
    #inverser playerTurn
    playerTurn = not playerTurn
    #Si checkVictory(1) renvoie true:
    if checkVictory(1):
        #afficher un message disant que l'utilisateur gagne
        print("\n\nThe user won!!")
        #quitter la boucle
        break
    #Sinon si checkVictory(2) renvoie true:
    elif checkVictory(2):
        #afficher un message disant que l'IA gagne
        print("\n\nThe CPU won!")
        #quitter la boucle
        break
    #Sinon si isGridFull() renvoie true
    elif isGridFull():
        #afficher une égalité
        print("Tie!")
        #quitter la boucle
        break
#afficher la grille
printGrid()