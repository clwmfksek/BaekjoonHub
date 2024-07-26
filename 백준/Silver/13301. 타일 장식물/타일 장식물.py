import sys
input = sys.stdin.readline

n = int(input())
dnp = [0] *(n+1)
if n == 0 : print(0)
elif n == 1 : print(4)
elif n == 2 : print(6)
else:
    dnp[0] = 0
    dnp[1] = 4
    dnp[2] = 6
    for i in range(3,n+1):
        dnp[i] = dnp[i-1] + dnp[i-2]
    print(dnp[n])