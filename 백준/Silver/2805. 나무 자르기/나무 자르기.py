import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lis = list(map(int,input().split()))

st = 0
en = max(lis)
maxnum = 0

while(st<=en):
    total = 0
    mid = (st+en)//2
    for i in lis:
        if i > mid:
            total += i - mid
    if total < m:
        en = mid - 1
    else :
        maxnum = mid
        st = mid + 1
print(maxnum)