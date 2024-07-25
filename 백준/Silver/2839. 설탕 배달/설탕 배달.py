import sys
inp = sys.stdin.readline
n = int(inp())
result = []
target = n // 3
for i in range(target+1):
    for j in range(target+1):
        if 3 * i + 5 * j == n:
            result.append(i+j)
if not result:
    print(-1)
else:
    print(min(result))    