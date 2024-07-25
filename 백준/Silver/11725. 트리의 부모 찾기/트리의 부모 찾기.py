import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for i in range(n+1)]

for i in range(n-1):
    num1,num2 = map(int,input().split())
    graph[num1].append(num2)
    graph[num2].append(num1)

visited = [0] * (n+1)
queue = deque()
queue.append(1)

def bfs():
    while(queue):
        temp = queue.popleft()
        for i in graph[temp]:
            if visited[i] == 0:
                visited[i] = temp
                queue.append(i)
bfs()
for i in range(2,n+1):
    print(visited[i])