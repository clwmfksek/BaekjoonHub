import sys
from collections import deque
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
nums = []
for i in range(N):
    nums.append(int(input()))

counts = [0] * (d + 1)
queue = deque()
result = 0
variety = 0 
for i in range(k):
    tar = nums[i % N]
    queue.append(tar)
    if counts[tar] == 0:
        variety += 1
    counts[tar] += 1

if counts[c] == 0:
    result = variety + 1
else:
    result = variety

for i in range(k, N + k):
    tar = nums[i % N]
    queue.append(tar)
    if counts[tar] == 0:
        variety += 1
    counts[tar] += 1

    target = queue.popleft()
    counts[target] -= 1
    if counts[target] == 0:
        variety -= 1

    if counts[c] == 0:
        result = max(result, variety + 1)
    else:
        result = max(result, variety)

print(result)
