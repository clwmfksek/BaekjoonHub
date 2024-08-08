import sys
input = sys.stdin.readline

n,m = map(int,input().split())

lis = []
for i in range(n):
    lis.append(list(map(int,input().split())))

res = [[0 for i in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        if j == 0 :
            res[i][j] = lis[i][j]
        else :
            res[i][j] = res[i][j-1] + lis[i][j]

for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    rest = 0
    if x1 == x2 and y1 == y2:
        print(lis[x1][y1])
    else :
        for i in range(x1,x2+1):
            if y1-1 < 0 :
                rest += res[i][y2]
            else :
                rest += res[i][y2] - res[i][y1-1]
        print(rest)