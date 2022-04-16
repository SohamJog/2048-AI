from moves import*
import random

MAXDEPTH = 4

fitness = {}
for i in range(4):
    fitness[i] = []

fitness[0] = [2048, 1024, 64, 32]
fitness[1] = [512, 128, 16, 2]
fitness[2] = [256, 8, 2, 1]
fitness[3] = [4, 2, 1, 1]



gradient_mat = [

			[[ 64,  16,  4,  0],[ 16,  4,  0, -4],[ 4,  0, -4, -16],[ 0, -4, -16, -64]], 
			
			[[ 0,  4,  16,  64],[-4,  0,  4,  16],[-16, -4,  0,  4],[-64, -16, -4, 0]],  
			
			[[ 0, -4, -16, -64],[ 4,  0, -4, -16],[ 16,  4,  0, -4],[ 64,  16,  4,  0]],  
			
			[[-64, -16, -4,  0],[-16, -4,  0,  4],[-4,  0,  4,  16],[ 0,  4,  16, 64]] 
]




def TerminalState(board):

    for i in range(4):
        for j in range(4):
            if(board[i][j] == 0): return False

    for i in range(4):
        for j in range(4):
            if(i+1<4 and board[i][j]==board[i+1][j]):
                return False
            if(j+1<4 and board[i][j]==board[i][j+1]):
                return False

    return True


def score(board):

    if(TerminalState(board)):
        return -1e9

    sum = [0,0,0,0]
    nonEmpty = 0
    mx = 0

    tot  = 0

    for i in range(4):
        for j in range(4):
            for k in range(4):
                mx = max(mx, board[j][k])
                tot+=board[j][k]
                sum[i]+=(board[j][k]**1.25)*gradient_mat[i][j][k]

    ret = max(sum)+(tot/2)
    if(mx!=board[0][0] and mx!=board[0][3] and mx!=board[3][0] and mx!=board[3][3]):
        ret/=2

    return ret
    '''h = {}

    h[0]  = [board[0][0],board[0][1],board[0][2],board[0][3],board[1][3],board[1][2],board[1][1],board[1][0],board[2][0],board[2][1],board[2][2],board[2][3],board[3][3],board[3][2],board[3][1],board[3][0]]
    h[1]  = [board[0][0],board[1][0],board[2][0],board[3][0],board[3][1],board[2][1],board[1][1],board[0][1],board[0][2],board[1][2],board[2][2],board[3][2],board[3][3],board[2][3],board[1][3],board[0][3]]
    h[2]  = [board[0][3],board[0][2],board[0][1],board[0][0],board[1][0],board[1][1],board[1][2],board[1][3],board[2][3],board[2][2],board[2][1],board[2][0],board[3][0],board[3][1],board[3][2],board[3][3]]
    h[3]  = [board[3][0],board[2][0],board[1][0],board[0][0],board[0][1],board[1][1],board[2][1],board[3][1],board[3][2],board[2][2],board[1][2],board[0][2],board[0][3],board[1][3],board[2][3],board[3][3]]
    h[4] = h[0]
    h[4].reverse()
    h[5] = h[1]
    h[5].reverse()
    h[6] = h[2]
    h[6].reverse()
    h[7] = h[3]
    h[7].reverse()

    penalties = [1,1,1,1,1,1,1,1]

    for i in range(1):
        for j in range(14):
         
            if(h[i][j]<=h[i][j+1] and h[i][j+1]<=h[i][j+2]):penalties[i]+=(h[i][j+1]**1.75)+(h[i][j+2]**1.5)
'''
    


def minimax(board,depth, alpha, beta, maximizingPlayer):

    if(TerminalState(board) or depth==MAXDEPTH):
        return score(board)

    brk = False

    if(maximizingPlayer):
        bestVal = -1e9
        #check left child
        if(brk==False):
            new_Board,dummy = move_left(board)
            value = minimax(new_Board,  depth+1, alpha, beta, False)
            bestVal = max(bestVal, value)
            if(beta<=bestVal):
                brk = True
            alpha = max(alpha, bestVal)


        #check right child
        if(brk==False):
            new_Board,dummy = move_right(board)
            value = minimax(new_Board,  depth+1, alpha, beta, False)
            bestVal = max(bestVal, value)
            if(beta<=bestVal):
                brk = True
            alpha = max(alpha, bestVal)


        #check up child
        if(brk==False):
            new_Board,dummy = move_up(board)
            value = minimax(new_Board,  depth+1, alpha, beta, False)
            bestVal = max(bestVal, value)
            alpha = max(alpha, bestVal)
            if(beta<=bestVal):
                brk = True
            alpha = max(alpha, bestVal)


        #check down child
        if(brk==False):
            new_Board,dummy = move_down(board)
            value = minimax(new_Board,  depth+1, alpha, beta, False)
            bestVal = max(bestVal, value)
            if(beta<=bestVal):
                brk = True
            alpha = max(alpha, bestVal)

        
        new_Board = board
        return bestVal
    
    else:

        Full = True
        for i in range(4):
            for j in range(4):
                if(board[i][j] == 0): Full = False

        if(Full): return minimax(board, depth+1, alpha, beta, True)
        bestVal = 1e15
        brk = False
        for i in range(4):
            if(brk):break
            for j in range(4):
                if(board[i][j]>0):continue
                new_Board = board
                new_Board[i][j] = 2

                value = minimax(new_Board, depth+1, alpha, beta, True)

                bestVal = min(bestVal, value)
                if(bestVal<=alpha):
                    brk = True
                    break
                beta = min(bestVal, beta)
                #########################
                #########################
                #########################
                new_Board = board
                new_Board[i][j] = 4

                value = minimax(new_Board, depth+1, alpha, beta, True)

                bestVal = min(bestVal, value)
                if(bestVal<=alpha):
                    brk = True
                    break
                beta = min(bestVal, beta)

        
        return bestVal

        
    


    
    


    

def findBestMovePlayer(board):

    if(TerminalState(board)):
        return "left"

    ret = ""
    bestScore = -1e9

    arr = []

    new_Board,dummy = move_left(board)
    k1 = minimax(new_Board, 0, -1e9, 1e15, True)
    print()
    print(f"left {k1}")
    if(k1>bestScore and dummy):
        ret = "left"
        bestScore = k1
        arr.clear()
        arr.append("left")

    
    

    new_Board,dummy = move_right(board)
    k2 = minimax(new_Board, 0, -1e9, 1e15, True)
    print(f"right {k2}")
    if(k2>bestScore and dummy):
        ret = "right"
        bestScore = k2
        arr.clear()
        arr.append("right")
    elif(k2==bestScore and dummy):
        arr.append("right")

    new_Board,dummy = move_up(board)
    k3 = minimax(new_Board, 0, -1e9, 1e15, True)
    print(f"up {k3}")
    if(k3>bestScore and dummy):
        ret = "up"
        bestScore = k3
        arr.clear()
        arr.append("up")
    elif(k3==bestScore and dummy):
        arr.append("up")

    new_Board,dummy = move_down(board)
    k4 = minimax(new_Board, 0, -1e9, 1e15, True)
    print(f"down {k4}")
    if(k4>bestScore and dummy):
        ret = "down"
        bestScore = k4
        arr.clear()
        arr.append("down")
    elif(k4==bestScore and dummy):
        arr.append("down")
    
    new_Board = board
    print(arr)
    ret = arr[random.randint(0,len(arr)-1)]

    return ret