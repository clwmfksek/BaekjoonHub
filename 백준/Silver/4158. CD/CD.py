import sys
from collections import Counter
inp = sys.stdin.readline

while True:
    n,m = map(int,inp().split())
    if n==0 and m==0: 
        break
    l1 = [int(inp()) for _ in range(n)]
    l2 = [int(inp()) for _ in range(m)]
    count = 0
    counter = Counter(l2)
    for i in l1:
        if i in counter:
            count += 1
    print(count)