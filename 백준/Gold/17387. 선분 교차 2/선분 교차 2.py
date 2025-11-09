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

t3 = where(x1,y1,x2,y2,x3,y3)
t4 = where(x1,y1,x2,y2,x4,y4)
t1 = where(x3,y3,x4,y4,x1,y1)
t2 = where(x3,y3,x4,y4,x2,y2)

cal1 = t3*t4
cal2 = t1*t2

if cal1 == cal2 == -1 or (cal1 == 0 and cal2 == -1) or (cal2 == 0 and cal1 == -1):
    print(1)
elif cal1 == 0 and cal2 == 0:
    if (t3 == 0 and t4 == 0) :
        if x1==x2==x3==x4:
            if (max(y1,y2) < min(y3,y4)):
                print(0)
            elif (max(y1,y2) > min(y3,y4)):
                if (max(y3,y4) < min(y1,y2)):
                    print(0)
                else :
                    print(1)
            else :
                print(1)
        else :
            if (max(x1,x2) < min(x3,x4)):
                print(0)
            elif (max(x1,x2) > min(x3,x4)):
                if (max(x3,x4) < min(x1,x2)):
                    print(0)
                else :
                    print(1)
            else :
                print(1)
    else : 
        print(1)
else :
    print(0)