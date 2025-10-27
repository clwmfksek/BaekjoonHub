import sys

input = sys.stdin.readline

n,m = map(int,input().split())
lis = list(map(int,input().split()))

lo = 0
hi = 1e9+1
while(lo <= hi):
    mid = int((lo + hi) // 2)
    cnt = 0
    for i in range(n):
        cnt += max(0,lis[i] - mid)
    if(cnt >= m):
        lo = mid + 1
    else:
        hi = mid - 1
print(lo-1)