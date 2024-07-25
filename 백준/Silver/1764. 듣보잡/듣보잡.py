import sys
from collections import Counter

n,m = map(int, sys.stdin.readline().split())
lis = []
lis2 = []
lis3 = []
for i in range(n):
    lis.append(sys.stdin.readline())
for i in range(m):
    lis2.append(sys.stdin.readline())
c = Counter(lis)

for i in lis2:
    if c[i] != 0:
        lis3.append(i)
print(len(lis3))
for i in sorted(lis3):
    print(i,end='')