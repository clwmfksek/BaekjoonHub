import sys
input = sys.stdin.readline

def where(x1,y1,x2,y2,x3,y3):
    cal = x1*y2 + x2*y3 + x3*y1 - y3*x1 - y1*x2 - y2*x3
    if cal > 0:
        return 1
    elif cal < 0:
        return -1
    else :
        return 0

def par(x1,x2,x3,x4,y1,y2,y3,y4):
    t3 = where(x1,y1,x2,y2,x3,y3)
    t4 = where(x1,y1,x2,y2,x4,y4)
    t1 = where(x3,y3,x4,y4,x1,y1)
    t2 = where(x3,y3,x4,y4,x2,y2)

    cal1 = t3*t4
    cal2 = t1*t2

    if cal1 == cal2 == -1 :
        return 2
    elif (cal1 == 0 and cal2 == -1) or (cal2 == 0 and cal1 == -1):
        return 1
    elif cal1 == 0 and cal2 == 0:
        if (t3 == 0 and t4 == 0) :
            if x1==x2==x3==x4:
                if (max(y1,y2) < min(y3,y4)):
                    return 0
                elif (max(y1,y2) > min(y3,y4)):
                    if (max(y3,y4) < min(y1,y2)):
                        return 0
                    elif (max(y3,y4) == min(y1,y2)):
                        return 1
                    else :
                        return 3
                else :
                    return 1
            else :
                if (max(x1,x2) < min(x3,x4)):
                    return 0
                elif (max(x1,x2) > min(x3,x4)):
                    if (max(x3,x4) < min(x1,x2)):
                        return 0
                    elif (max(x3,x4) == min(x1,x2)):
                        return 1
                    else :
                        return 3
                else :
                    return 1
        else : 
            return 1
    else :
        return 0


n = int(input())
lis = [list(map(int,input().split())) for i in range(n)]
maps = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(i+1):
        ans = par(lis[i][0],lis[i][2],lis[j][0],lis[j][2],lis[i][1],lis[i][3],lis[j][1],lis[j][3])
        maps[i][j] = ans
        maps[j][i] = ans
for i in range(n):
    for j in range(n):
        if i == j : print(3,end='')
        else : print(maps[i][j],end='')
    print()