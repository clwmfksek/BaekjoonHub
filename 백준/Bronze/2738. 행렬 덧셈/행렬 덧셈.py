import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

n,m = map(int,input().split())
lis1 = []
lis2 = []
res = []
for j in range(n):
    lis1.append(list(map(int,input().split())))
for j in range(n):
    lis2.append(list(map(int,input().split())))

for i in range(n):
    v = []
    for j in range(m):
        v.append(lis1[i][j] + lis2[i][j])
    res.append(v)
for i in res:
    for j in i:
        print(j,end=' ')
    print()