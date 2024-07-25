import sys
from collections import Counter
inp = sys.stdin.readline
n,m = map(int,inp().rstrip().split())
li1 = []
li2 = []
count = 0
for _ in range(n):
    li1.append(inp().rstrip())
for _ in range(m):
    li2.append(inp().rstrip())
c = Counter(li1)
for i in li2:
    if i in c:
        count += 1
print(count)