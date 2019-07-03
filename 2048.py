from random import randint

#Function to add a new piece
#The backend is using exponents, but printBoard actually converts it to the right thing
def addNum():
    x=randint(0,3)
    y=randint(0,3)
    while(board[x][y]!='-'):
        x=randint(0,3)
        y=randint(0,3)
    rng=randint(1,20)
    if(rng==20):
        board[x][y]=2
    else:
        board[x][y]=1

#The default 2048 board
board=[['-','-','-','-'],['-','-','-','-'],['-','-','-','-'],['-','-','-','-']]
#Set two random spots to equal 1
addNum()
addNum()

#Prints the board
#Note that 2**24 will be 8 digits, which this board won't support
def printBoard():
    rowEnd="┣━━━━━━━╋━━━━━━━╋━━━━━━━╋━━━━━━━┫"
    rowBuf="┃       ┃       ┃       ┃       ┃"
    for y in range(0,4):
        if(y==0):
            print("┏━━━━━━━┳━━━━━━━┳━━━━━━━┳━━━━━━━┓")
        else:
            print(rowEnd)
        print(rowBuf)
        print("┃",end="")
        for x in range(0,4):
            if(board[x][y]=='-'):
                print("       ┃",end="")
            else:
                real=2**board[x][y]
                spaces=7-len(str(real))
                hspaces=round(spaces/2)
                for i in range(0,hspaces):
                    print(" ",end="")
                print(2**board[x][y],end="")
                for i in range(0,spaces-hspaces):
                    print(" ",end="")
                print("┃",end="")
        print()
    print("┗━━━━━━━┻━━━━━━━┻━━━━━━━┻━━━━━━━┛")

#What happens when you send gravity upwards
def upGrav():
    for x in range (0,4):
        #Move anything that can
        for repeat in range(0,3):
            for y in range (3,0,-1):
                if(board[x][y-1]=='-'):
                    temp=board[x][y]
                    board[x][y]=board[x][y-1]
                    board[x][y-1]=temp
        #Merge anything adjacent to the same kind
        for y in range (1,4):
            if(board[x][y]==board[x][y-1] and board[x][y]!='-'):
                board[x][y-1]+=1
                board[x][y]='-'
                y-=1
        #Move again
        for repeat in range(0,3):
            for y in range (3,0,-1):
                if(board[x][y-1]=='-'):
                    temp=board[x][y]
                    board[x][y]=board[x][y-1]
                    board[x][y-1]=temp

#What happens when you send gravity downwards
def downGrav():
    for x in range (0,4):
        #Move anything that can
        for repeat in range(0,3):
            for y in range (0,3):
                if(board[x][y+1]=='-'):
                    temp=board[x][y]
                    board[x][y]=board[x][y+1]
                    board[x][y+1]=temp
        #Merge anything adjacent to the same kind
        for y in range (2,-1,-1):
            if(board[x][y]==board[x][y+1] and board[x][y]!='-'):
                board[x][y+1]+=1
                board[x][y]='-'
                y+=1
        #Move again
        for repeat in range(0,3):
            for y in range (0,3):
                if(board[x][y+1]=='-'):
                    temp=board[x][y]
                    board[x][y]=board[x][y+1]
                    board[x][y+1]=temp

#What happens when you send gravity to the left
def leftGrav():
    for y in range (0,4):
        #Move anything that can
        for repeat in range(0,3):
            for x in range (3,0,-1):
                if(board[x-1][y]=='-'):
                    temp=board[x][y]
                    board[x][y]=board[x-1][y]
                    board[x-1][y]=temp
        #Merge anything adjacent to the same kind
        for x in range (1,4):
            if(board[x][y]==board[x-1][y] and board[x][y]!='-'):
                board[x-1][y]+=1
                board[x][y]='-'
                x-=1
        #Move again
        for repeat in range(0,3):
            for x in range (3,0,-1):
                if(board[x-1][y]=='-'):
                    temp=board[x][y]
                    board[x][y]=board[x-1][y]
                    board[x-1][y]=temp

#What happens when you send gravity to the right
def rightGrav():
    for y in range (0,4):
        #Move anything that can
        for repeat in range(0,3):
            for x in range (0,3):
                if(board[x+1][y]=='-'):
                    temp=board[x][y]
                    board[x][y]=board[x+1][y]
                    board[x+1][y]=temp
        #Merge anything adjacent to the same kind
        for x in range (2,-1,-1):
            if(board[x][y]==board[x+1][y] and board[x][y]!='-'):
                board[x+1][y]+=1
                board[x][y]='-'   
                x+=1
        #Move again
        for repeat in range(0,3):
            for x in range (0,3):
                if(board[x+1][y]=='-'):
                    temp=board[x][y]
                    board[x][y]=board[x+1][y]
                    board[x+1][y]=temp

#returns true if both boards are the Same
def sameBoards(board1,board2):
    for y in range(0,4):
        for x in range(0,4):
            if(board1[x][y]!=board2[x][y]):
                return False
    return True

#returns a deep copy version of board1
def archiveBoard(board1):
    arc=[['-','-','-','-'],['-','-','-','-'],['-','-','-','-'],['-','-','-','-']]
    for y in range(0,4):
        for x in range(0,4):
            arc[x][y]=board1[x][y]
    return arc

#Checks if there are any possible moves
def canMove():
    for y in range(0,4):
        for x in range(0,3):
            if(board[x][y]==board[x+1][y] or board[x+1][y]=='-'):
                return True
        for x in range(3,0,-1):
            if(board[x][y]==board[x-1][y] or board[x-1][y]=='-'):
                return True
    for x in range(0,4):
        for y in range(0,3):
            if(board[x][y]==board[x][y+1] or board[x][y+1]=='-'):
                return True
        for y in range(3,0,-1):
            if(board[x][y]==board[x][y-1] or board[x][y-1]=='-'):
                return True
    return False


while(True):
    printBoard()
    if(not canMove()):
        print("No valid moves remain.")
        break
    tempBoard=archiveBoard(board)
    print("  W        You can also quit by typing \'quit\'")
    dir=input("A S D             ")
    if(dir.lower()=='quit'):
        break
    elif(dir.lower()=='w'):
        upGrav()
    elif(dir.lower()=='a'):
        leftGrav()
    elif(dir.lower()=='s'):
        downGrav()
    elif(dir.lower()=='d'):
        rightGrav()
    if(not sameBoards(tempBoard, board)):
        addNum()
    print()
    print()

#This isn't a perfect representation like, at all
#TODO: Fix physics with merges- double merge still occurs but rarely, definite corner case