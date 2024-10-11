import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lis = [int(input()) for i in range(n)]
lis.sort()

start = 1
end = lis[-1] - lis[0]
ans = 0
while(start<=end):
    mid = (start+end)//2
    cur = lis[0]
    count = 1
    
    for i in range(1,n):
        if lis[i] >= cur + mid:
            count += 1
            cur = lis[i]
    
    if count >= m:
        start = mid + 1
        ans = mid
    else :
        end = mid - 1

print(ans)