import sys
from collections import Counter

input = sys.stdin.readline
N = int(input())
books = list(input().rstrip() for _ in range(N))

c = Counter(books)

# 가장 많이 팔린 책 권수
maximum = max(c.values())
ans = []
for key, value in c.items():
    if value >= maximum:
        maximum = value
        ans.append(key)

ans.sort()
print(ans[0])