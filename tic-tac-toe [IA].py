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

# Déclarer une variable booléan firstPlayerChoice et lui assigner la valeur True
firstPlayerChoice = True

#Définir printGrid qui affiche la grille du jeu
def printGrid():
    # Assigner 1 à une variable index
    index = 1

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
                # Si firstPlayerChoice est égal à True
                if firstPlayerChoice:
                    # Affichier index
                    print(index, end="")
                else:
                    # Afficher un espace vide
                    print(" ", end="")
                index=index+1
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

#définir une fonction CPUChoice qui permettra à l'IA de faire des choix
def CPUChoice():
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
#afficher un message montrant que l'utilisateur possède les O et le CPU les X
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
                    print("The chosen box is already taken.")
            #si l'essai echoue:
            except:
                #mettre choix à None
                choice = None
                #afficher un message disant que la réponse doit être un entier
                print("The user choice should be an integer")
    #Sinon:
    else:
        #afficher un message disant que l'IA doit jouer
        print("It's the CPU's turn!")
        #Tant que choice vaut None ou que la case choisie est prise
        while choice==None or not checkGrid(choice):
            #assigner ce que retourne CPUChoice à choice
            choice = CPUChoice()
    #assigner à x, y ce que retourne convertToGridIndex(choice)
    x, y = convertToGridIndex(choice)
    #assigner à la grid en position x, y 1 ou 2 suivant si playerTurn est True ou False
    grid[x][y] = playerTurn and 1 or 2
    #mettre choice à None
    choice = None
    # Si playerTurn est True et que firstPlayerChoice est True
    if playerTurn and firstPlayerChoice:
        # Assigner False à firstPlayerChoice
        firstPlayerChoice = False
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