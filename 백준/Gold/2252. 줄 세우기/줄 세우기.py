import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())

node = [0] * (n)

lis = [[] for i in range(n)]
for i in range(m):
    n1,n2 = map(int,input().split())
    n1 -= 1
    n2 -= 1
    node[n2] += 1
    lis[n1].append(n2)

queue = deque()

for i in range(n):
    if node[i] == 0 :
        queue.append(i)
answer = []
while(queue):
    s = queue.popleft()
    answer.append(s+1)
    for i in lis[s]:
        node[i] -= 1
        if node[i] == 0:
            queue.append(i)
print(*answer)