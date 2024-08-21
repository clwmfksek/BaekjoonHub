import sys
input = sys.stdin.readline
from collections import deque

n,k = map(int,input().split())

visited = [0] * 100001
result = []

queue = deque([])
queue.append(n)

while(queue):
    target = queue.popleft()
    if target == k :
        result.append(visited[target])
        continue
    for i in [target+1,target-1,target*2]:
        if 0 <= i <= 100000 and (visited[i] == 0 or visited[i] == visited[target] + 1):
            visited[i] = visited[target] + 1
            queue.append(i)

print(result[0])
print(len(result))