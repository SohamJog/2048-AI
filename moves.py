
#left, right, down, up



def lg(num):
    if(num==0): return 0
    if(num==2): return 1
    if(num==4): return 2
    if(num==8): return 3
    if(num==16): return 4
    if(num==32): return 5
    if(num==64): return 6
    if(num==128): return 7
    if(num==256): return 8
    if(num==512): return 9
    if(num==1024): return 10
    if(num==2048): return 11
    return 12




def transpose(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat



def move_up(board):

    ok = False
    just = True

    ret = {}

    for i in range(4):
        X = []
        j = 0
        while(j<4):
            if(just == False):
                if(len(X)>0 and X[len(X)-1]==board[i][j]):
                    just = True
                    el = X.pop()*2
                    X.append(el)
                else:
                    if(board[i][j]!=0):X.append(board[i][j])
            elif(board[i][j]!=0):
                X.append(board[i][j])
                just = False
            j+=1          
            
        while(len(X)<4):
            X.append(0)
        ret[i] = X
    
    for i in range(4):
        for j in range(4):
            if(board[i][j]!=ret[i][j]): ok=True

    return ret,ok

    

def move_down(board):

    ok = False
    just = True

    ret = {}

    for i in range(4):
        X = []
        j = 3
        
        while(j>=0):
            if(just == False):
                if(len(X)>0 and X[len(X)-1]==board[i][j]):
                    just = True
                    el = X.pop()*2
                    X.append(el)
                else:
                    if(board[i][j]!=0):X.append(board[i][j])
            elif(board[i][j]!=0):
                X.append(board[i][j])
                just = False
            j-=1       
        

        #X.reverse()
        while(len(X)<4):
            X.append(0)
        X.reverse()
        ret[i] = X
    
    for i in range(4):
        for j in range(4):
            if(board[i][j]!=ret[i][j]): ok=True

    return ret,ok



def move_left(board):
    
    ok = False
    ret = transpose(board)
    ret,ok = move_up(ret)
    ret = transpose(ret)
    return ret,ok


def move_right(board):

    ok = False
    ret = transpose(board)
    ret,ok = move_down(ret)
    ret = transpose(ret)
    return ret,ok
    
    
