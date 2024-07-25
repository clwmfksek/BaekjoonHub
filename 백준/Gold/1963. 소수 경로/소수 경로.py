import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque


n=10000
a = [False,False] + [True]*(n-1)
sosu=[]

for i in range(2,n+1):
  if a[i]:
    sosu.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False

def bfs(n1,n2):
    visited[n1] = 1
    queue = deque([(n1)])
    while(queue):
        number = queue.popleft()
        if number == n2 : 
            print(visited[number]-1)
            return
        for j in range(10):
            for i in range(4):
                x = list(str(number))
                x[i] = str(j)
                x = int(''.join(x))
                if x >= 10000: continue
                if x < 1000 or visited[x] != 0 : continue
                if not a[x] : continue
                visited[x] = visited[number] + 1
                queue.append(x)


t = int(input())

for i in range(t):
    num1,num2 = map(int,input().split())
    visited = [0 for i in range(10000)]
    bfs(num1,num2)
