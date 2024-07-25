import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

t = int(input())

for _ in range(t):
    target = str(bin(int(input())))[2:][::-1]
    for i in range(len(target)):
        if target[i] == '1' : print(i,end=' ')