import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

num1,num2 = map(int,input().split())

lis = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = ''
while num1>0:
    ans += str(lis[num1%num2])
    num1 = num1//num2

print(ans[::-1])