import sys
input = sys.stdin.readline

n = int(input())

data = list(map(int, input().split()))
data.sort(reverse=True)

res = []
for i in range(n):
    res.append(data[i]+ 1 + i)

print(max(res) + 1)