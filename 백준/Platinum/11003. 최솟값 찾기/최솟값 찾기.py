import sys
from collections import deque
input = sys.stdin.readline
n,m=map(int,input().split())
lis = list(map(int,input().split()))
lis2 = deque([])
for i in range(n):
   if lis2 and lis2[0][1] < i-m+1:
    lis2.popleft()
   while len(lis2) > 0 and lis2[-1][0] > lis[i]:
    lis2.pop()
   lis2.append((lis[i],i))
   print(lis2[0][0],end=" ")