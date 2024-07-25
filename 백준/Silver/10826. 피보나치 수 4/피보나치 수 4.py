import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

fibo = [0] * 10001
n = int(input())
fibo[0] = 0
fibo[1] = 1

for i in range(2,n+1):
    fibo[i] = fibo[i-1] + fibo[i-2]
print(fibo[n])