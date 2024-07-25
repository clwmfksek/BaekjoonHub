import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

inp = ""
while True:
    lis = [0] * 26
    inp = list(input().rstrip())
    if (ord(inp[0]) == 35):
        break
    for i in inp:
        if i.isalpha():
            lis[(ord(i.lower()))-97] = 1
        else  : continue
    print(lis.count(1))