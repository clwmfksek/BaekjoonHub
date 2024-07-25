import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

m = int(input())

dp = [0] * 101
dp[1] = dp[2] = dp[3] = 1
for i in range(4,101):
    dp[i] = dp[i-2] + dp[i-3]

for _ in range(m):
    num = int(input())
    print(dp[num])