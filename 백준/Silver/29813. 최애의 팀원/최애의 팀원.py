import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

n = int(input())
queue = []
for _ in range(n):
    n,m = input().rstrip().split()
    m = int(m)
    queue.append([n,m])

while(len(queue)>1):
    for i in range(queue[0][1]-1):
        queue.append(queue.pop(1))
    queue.pop(0)
    queue.pop(0)
print(queue[0][0])
