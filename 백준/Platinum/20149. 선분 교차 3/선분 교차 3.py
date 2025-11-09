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

x1,y1,x2,y2 = map(int,input().split())
x3,y3,x4,y4 = map(int,input().split())

def cross():
    A1 = y2 - y1
    B1 = x1 - x2
    C1 = A1 * x1 + B1 * y1

    A2 = y4 - y3
    B2 = x3 - x4
    C2 = A2 * x3 + B2 * y3

    determinant = A1 * B2 - A2 * B1
    
    x = (B2 * C1 - B1 * C2) / determinant
    y = (A1 * C2 - A2 * C1) / determinant
    if x.is_integer():
        x = int(x)
    if y.is_integer():
        y = int(y)
    return (x, y)

t3 = where(x1,y1,x2,y2,x3,y3)
t4 = where(x1,y1,x2,y2,x4,y4)
t1 = where(x3,y3,x4,y4,x1,y1)
t2 = where(x3,y3,x4,y4,x2,y2)

cal1 = t3*t4
cal2 = t1*t2

if cal1 == cal2 == -1 or (cal1 == 0 and cal2 == -1) or (cal2 == 0 and cal1 == -1): # 둘다 -1이면 겹치는 점 1개가 선분 내에 있고, -1 0 또는 0 -1 일 경우에는 한 점에서 겹친다.
    print(1)
    print(*cross())
elif cal1 == 0 and cal2 == 0:
    if (t3 == 0 and t4 == 0) : # 한 직선 내에 두 선분이 있다.
        if x1==x2==x3==x4:
            if (max(y1,y2) < min(y3,y4)): # 선분 c1이 선분 c2 아래에 있다
                print(0)
            elif (max(y1,y2) > min(y3,y4)): # 선분 c1이 선분 c2 위에 있다
                if (max(y3,y4) < min(y1,y2)): # 교점이 없으면
                    print(0)
                elif (max(y3,y4) == min(y1,y2)): # 교점이 하나면
                    print(1)
                    maxnum = max(y3,y4)
                    if maxnum == y3 :
                        print(x3,y3)
                    else :
                        print(x4,y4)
                else : # 교점이 여러개면
                    print(1)
            else : # 선분 c1의 최고점과 선분 c2의 최저점이 같다
                print(1)
                maxnum = max(y1,y2)
                if maxnum == y1 :
                    print(x1,y1)
                else :
                    print(x2,y2)
        else :
            if (max(x1,x2) < min(x3,x4)):
                print(0)
            elif (max(x1,x2) > min(x3,x4)):
                if (max(x3,x4) < min(x1,x2)):
                    print(0)
                elif (max(x3,x4) == min(x1,x2)):
                    print(1)
                    maxnum = max(x3,x4)
                    if maxnum == x3 :
                        print(x3,y3)
                    else :
                        print(x4,y4)
                else :
                    print(1)
            else :
                print(1)
                maxnum = max(x1,x2)
                if maxnum == x1 :
                    print(x1,y1)
                else :
                    print(x2,y2)
    else : 
        print(1)
        print(*cross())
else :
    print(0)