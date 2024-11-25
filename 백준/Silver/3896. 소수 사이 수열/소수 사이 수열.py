import sys
input = sys.stdin.readline

res = [0, 0] + [1] * (1299709 - 1)
primes = []
for i in range(2, 1299710):
    if res[i]:
        primes.append(i)
        for j in range(2 * i, 1299710, i):
            res[j] = 0
n = int(input())
for _ in range(n):
    num = int(input())
    if res[num]: 
        print(0)
    else:
        start = num
        while start > 0 and not res[start]:
            start -= 1
        end = num
        while end < 1299710 and not res[end]:
            end += 1
        print(end - start)