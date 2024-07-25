import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

n = int(input())
INF = sys.maxsize
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))


for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[k][j] ==1 and graph[i][k] == 1 :
                graph[i][j] = 1
    
for i in range(n):
    for j in range(n):
        print(graph[i][j], end=' ')
    print()