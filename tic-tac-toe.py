import random

grid = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

playerTurn = random.randint(0, 1)==0
print(playerTurn)

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
    print(x)
    print(x//3)
    if x<=3:
        x, y = 0, x-1
    elif x<=6:
        x, y = 1, x-4
    else:
        x, y = 2, x-7
    return x, y

def checkVictory():
    verif = 0
    # Vertical lines
    for i in grid:
        for j in i:
            if j==1:
                verif=verif+1
            else:
                verif = 0
                break
    
    for i in range(0,2):
        for j in range(0, 2):
            if grid[i][j]==1:
                verif = verif + 1
            else:
                verif = -999
    


while True:
    printGrid()
    if playerTurn:
        while choice==None or not checkGrid(choice):
            choice = input("It's your turn! (1-9) ")
            try:
                choice = int(choice)
                if choice<1 or choice>9:
                    raise IndexError
            except:
                raise TypeError(f"The user choice should be an integer")
    else:
        while choice==None or not checkGrid(choice):
            print("It's the ordi's turn!")
            choice = random.randint(1, 9)
    x, y = convertToGridIndex(choice)

    print(x, y)
    grid[x][y] = playerTurn and 1 or 2
    choice = None
    playerTurn = not playerTurn

    checkVictory()