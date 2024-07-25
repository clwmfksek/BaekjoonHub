import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

inp = list(input().rstrip())
res = 0
lis = [['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','R','Q','S'],['T','U','V'],['W','X','Y','Z']]
for i in inp:
    for j in range(len(lis)):
        if i in lis[j]:
            res += j+3
print(res)