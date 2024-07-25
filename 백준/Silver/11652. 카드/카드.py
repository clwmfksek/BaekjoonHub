import sys
from collections import Counter
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
li = []
for i in range(n):
    li.append(int(input()))
c = Counter(sorted(li))
print(c.most_common(1)[0][0])