from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(n)]
visited = [[0] * m for i in range(n)]
pos = deque([])

for i in range(n):
    for j in range(m):
        if graph[i][j]:
            pos.append((i, j))

dx = [1, 1, 0, 0, -1, -1, 1, -1]
dy = [1, -1, 1, -1, 1, -1, 0, 0]
result = 0
while pos:
    x, y = pos.popleft()
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= n or nx < 0 or ny >= m or ny < 0: continue
        if graph[nx][ny] != 0 : continue
        pos.append([nx, ny])
        graph[nx][ny] = graph[x][y] + 1
        result = max(result,graph[nx][ny])
print(result-1)
