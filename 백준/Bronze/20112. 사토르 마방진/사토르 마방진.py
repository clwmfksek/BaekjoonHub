import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

n = int(input())
graph = []

for i in range(n):
    graph.append(list(input().rstrip()))
bol = True
for i in range(n):
    for j in range(i+1,n):
        if graph[i][j] != graph[j][i]:
            bol = False
            break
if(bol): print("YES")
else : print("NO")