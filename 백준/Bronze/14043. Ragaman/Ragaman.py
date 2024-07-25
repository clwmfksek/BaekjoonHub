import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def solve():
    inp1 = list(input().rstrip())
    inp2 = list(input().rstrip())

    count = [0 for i in range(26)]

    for i in range(len(inp1)):
        count[ord(inp1[i])-97] += 1
        if(inp2[i] == '*'): continue
        count[ord(inp2[i])-97] -= 1

    ans = inp2.count('*')
    for i in range(26):
        if count[i] > 0: ans -= count[i]

    return ans == 0

if solve(): print("A")
else : print("N")