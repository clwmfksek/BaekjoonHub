import sys
input = sys.stdin.readline

lis = []

for i in range(9):
    lis.append(list(map(int,input().rstrip())))

zerodiv = []
for i in range(9):
    for j in range(9):
        if lis[i][j] == 0:
            zerodiv.append([i,j])

def rowcheck(r,v):
    for i in range(9):
        if lis[r][i] == v :
            return False
    return True


def colcheck(c,v):
    for i in range(9):
        if lis[i][c] == v :
            return False
    return True

def boxcheck(r,c,v):
    r1 = (r//3)*3
    c1 = (c//3)*3
    for i in range(3):
        for j in range(3):
            if lis[r1+i][c1+j] == v:
                return False
    return True

def dfs(depth):
    if depth >= len(zerodiv):
        for j in range(9):
            print(''.join(map(str,lis[j])))
        exit()
    
    nr,nc = zerodiv[depth]
    for i in range(1,10):
        if rowcheck(nr,i) and colcheck(nc,i) and boxcheck(nr,nc,i):
            lis[nr][nc] = i
            dfs(depth+1)
            lis[nr][nc] = 0
dfs(0)