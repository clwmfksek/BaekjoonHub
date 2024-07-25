import sys
inp = sys.stdin.readline
n = int(inp())
mid = round((2*n-1) / 2,2) 
m = 2*n-1

for i in range(2*n-1):
    if i <= mid:
        target = i
        for k in range(target):
            print(" ",end='')
        for j in range(m-2*i):
            print("*",end='')
    else :
        target = 2*(i - mid) + 2
        for j in range(2 * int(mid) - i):
            print(" ",end='')
        for k in range(int(target)):
            print("*",end='')
    print("\n",end='')