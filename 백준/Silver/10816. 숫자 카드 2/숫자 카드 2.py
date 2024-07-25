import sys
from collections import Counter

n = int(sys.stdin.readline())
lis = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
lis2 = list(map(int, sys.stdin.readline().split()))

c = Counter(lis)
for i in lis2:
    print(c[i], end=' ')