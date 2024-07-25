import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m = input().rstrip().split()
if(n[::-1]>m[::-1]) : print(n[::-1])
else : print(m[::-1])