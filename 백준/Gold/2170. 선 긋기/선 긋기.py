import sys
input = sys.stdin.readline
n = int(input())
lis = [list(map(int,input().split())) for i in range(n)]
lis.sort()

start = -1000000001
end = -1000000001
ans = 0
for i in range(n):
    if lis[i][0] >= start and lis[i][0] <= end:
        if lis[i][1] - end > 0:
            ans += abs(lis[i][1] - end)
            end = lis[i][1]
    elif lis[i][0] > end:
        start = lis[i][0]
        end = lis[i][1]
        ans += abs(end-start)
print(ans)