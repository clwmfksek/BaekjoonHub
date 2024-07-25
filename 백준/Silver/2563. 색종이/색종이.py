import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

n = int(input())
paper = [[0]*101 for i in range(101)]
for _ in range(n):
    n,m = map(int,input().split())
    for i in range(n,n+10):
        for j in range(m,m+10):
            paper[i][j] = 1

result = 0
for i in range(101):
    for j in range(101):
        if paper[i][j] == 1 :result += 1
print(result)