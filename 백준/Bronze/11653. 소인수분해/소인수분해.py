import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

sosu = [False] + [False] + [True] * (n-1)
primes = []

for i in range(2,n+1):
    if sosu[i]:
        primes.append(i)
        for j in range(2*i,n+1,i):
            sosu[j] = False
result = []
while(n!=1):
    for i in primes:
        if n%i == 0:
            result.append(i)
            n = n//i
for i in sorted(result):
    print(i)