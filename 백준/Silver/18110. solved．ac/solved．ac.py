import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
li = []
for _ in range(n):
    li.append(int(input()))
li.sort()

def roundUp(x):
    if (x - int(x)) >= 0.5:
        return int(x) + 1
    else:
        return int(x)
    
cut = roundUp(n*0.15)
if (len(li[cut:n-cut]) > 0):
    print(roundUp(sum(li[cut:n-cut])/len(li[cut:n-cut])))
else :
    print(0)