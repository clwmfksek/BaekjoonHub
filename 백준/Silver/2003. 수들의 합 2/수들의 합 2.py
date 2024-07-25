import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())
li = list(map(int,input().split()))

en = 0
total_sum = 0
count = 0

for i in range(n):
    while(en<n and total_sum < m):
        total_sum += li[en]
        en += 1
    if total_sum == m:
        count += 1
    total_sum -= li[i]
print(count)
