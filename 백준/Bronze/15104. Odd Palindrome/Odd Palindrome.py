import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque
s = input().rstrip()
bol = True
for i in range(1,len(s)):
    if s[i] == s[i-1] : 
        bol = False
        break
if(bol) : print("Odd.")
else : print("Or not.")