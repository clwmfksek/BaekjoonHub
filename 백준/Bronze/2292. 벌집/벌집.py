import sys
inp = sys.stdin.readline
num = int(inp().rstrip())
n = 1
while(1):
    if num == 1:
        print(1)
        break
    else :
        if num <= 3*n*(n+1)+1 and num >= 3*(n-1)*n+1:
            print(n+1)
            break
        else : n += 1