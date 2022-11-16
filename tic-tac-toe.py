import random

grid = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

playerTurn = False#random.randint(0, 1)==0

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
    x = x-1
    if x<0:
        x, y = 0, 0
    elif x<2:
        x, y = 0, x
    elif x<5:
        x, y = 1, x-3
    elif x<8:
        x, y = 2, x-6
    return x, y

def convertToNormalIndex(x:int, y:int)->int:
    return ((y*3)+x)+1

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
    corners = [1, 3, 7, 9]
    random.shuffle(corners)

    ligne = 0
    possibleLastBox = None
    print(possibleLastBox)
    for x in range(3):
        for y in range(3):
            if grid[x][y]==1:
                ligne=ligne+1
            else:
                if possibleLastBox!=None:
                    break
                possibleLastBox = convertToNormalIndex(x, y)
        if ligne == 2:
            print("Blocked!")
            return possibleLastBox
        else:
            ligne = 0
            possibleLastBox = None

    for y in range(3):
        for x in range(3):
            if grid[x][y]==1:
                ligne=ligne+1
            else:
                if possibleLastBox!=None:
                    break
                possibleLastBox = convertToNormalIndex(x, y)
        if ligne == 2:
            print("Blocked!")
            return possibleLastBox
        else:
            ligne = 0
            possibleLastBox = None

    if getBoxValue(5)==0:
        print("Center")
        return 5

    for i in corners:
        if getBoxValue(i)==0:
            print("Corner")
            return i
    print("Random")
    return random.randint(1, 9)
                
    


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
printGrid()