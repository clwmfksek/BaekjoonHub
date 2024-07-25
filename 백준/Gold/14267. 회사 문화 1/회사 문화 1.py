import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lis = list(map(int,input().split()))
dp = [0] * (n+1)

for i in range(m):
    num1,num2 = map(int,input().split())
    dp[num1] += num2

for i in range(2,n+1):
    dp[i] += dp[lis[i-1]]

dp.pop(0)
print(*dp)