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

cal1 = where(x1,y1,x2,y2,x3,y3) * where(x1,y1,x2,y2,x4,y4)
cal2 = where(x3,y3,x4,y4,x1,y1) * where(x3,y3,x4,y4,x2,y2)

if cal1 == cal2 == -1:
    print(1)
else : 
    print(0)