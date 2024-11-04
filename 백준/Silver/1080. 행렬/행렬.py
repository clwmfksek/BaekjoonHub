import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lis1 = [list(map(int,list(input().rstrip()))) for i in range(n)]
lis2 = [list(map(int,list(input().rstrip()))) for i in range(n)]
if (n < 3 or m < 3) and lis1 != lis2 : print(-1)
else :
    count = 0
    for i in range(n-2):
        for j in range(m-2):
            if lis1[i][j] != lis2[i][j]:
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        if lis1[k][l] == 1: lis1[k][l] = 0
                        else : lis1[k][l] = 1
                count += 1
    if lis1 == lis2 : print(count)
    else : print(-1)