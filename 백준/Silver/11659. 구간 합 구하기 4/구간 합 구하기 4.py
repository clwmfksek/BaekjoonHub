import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

n,m = map(int,input().split())
lis = list(map(int,input().split()))
lists = [0 for i in range(n+1)]
lists[1] = lis[0]
for i in range(2,n+1):
    lists[i] = lis[i-1] + lists[i-1]
for i in range(m):
    num1,num2 = map(int,input().split())
    print(lists[num2] - lists[num1-1])