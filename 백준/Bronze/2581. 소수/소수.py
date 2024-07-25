import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

sosu = []

m = int(input())
n = int(input())
sosu = [True] * (n+1)
primes = []
sosu[0] = False
sosu[1] = False
for i in range(2,n+1):
    if sosu[i]:
        primes.append(i)
        for j in range(2*i,n+1,i):
            sosu[j] = False
result = 0
minn = sys.maxsize
for i in range(m,n+1):
    if sosu[i] == True:
        result += i
        minn = min(minn,i)
if result :
    print(result)
    print(minn)
else : print(-1)