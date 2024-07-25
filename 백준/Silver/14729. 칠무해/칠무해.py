import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
li = []
for i in range(n):
    li.append(float(input()))
li.sort()
for i in range(7):
    print('{:.3f}'.format(li[i]))