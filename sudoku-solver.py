import numpy as np

m0=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

def check(b,a,n):
    n=str(n)
    global m0
    if(not n in m0[b]):
        for i in range(9):
            if n == m0[i][a]:
                return False
        if b%3 == 1:
            b = b-1
        elif b%3 == 2:
            b = b-2
            
        if a%3 == 1:
            a = a-1
        elif a%3 == 2:
            a = a-2
            
        for i in range(3):
            for j in range(3):
                if(m0[b+i][a+j] == n):
                    return False
        return True
    else:
        return False
        
def solve(y,x):
    global m0
    print(np.matrix(m0))
    original=m0[y][x]
    if(m0[y][x] == "."):
        for k in range(1,10,1):
            if(check(y,x,k)):
                m0[y][x]=str(k)
                if(x == 8 and y == 8):
                    print(np.matrix(m0))
                    return True
                if(x == 8 and y != 8):
                    if(solve(y+1,0)):
                        return True
                else:
                    if(solve(y,x+1)):
                        return True

        m0[y][x]="."
        return False
    else:
        if(x == 8 and y == 8):
            print(np.matrix(m0))
            return True
        if(x == 8 and y != 8):
            if(solve(y+1,0)):
                return True
            else:
                return False
        else:
            if(solve(y,x+1)):
                return True
            else:
                return False
            

solve(0,0)



