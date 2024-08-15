import sys
input = sys.stdin.readline

N,T = map(int,input().split())
K = [0]
S = [0]
dp = [[0]*(T+1) for i in range(N+1)]

for i in range(N):
    n1,n2 = map(int,input().split())
    K.append(n1)
    S.append(n2)

for i in range(1,N+1):
    for j in range(1,T+1):
        if j >= K[i]:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-K[i]]+S[i])
        else :
            dp[i][j] = dp[i-1][j]

print(dp[N][T])