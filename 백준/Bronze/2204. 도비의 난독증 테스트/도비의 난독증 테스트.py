import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

while(True):
    t = int(input())
    if t == 0 : break
    
    lis = []
    for _ in range(t):
        lis.append(input().rstrip())
    lis.sort(key=str.lower)
    print(lis[0])