import sys
input = sys.stdin.readline

N,M = map(int,input().split())
v = []
w = []
for i in range(M):
    n1,n2 = map(int,input().split())
    v.append(n1)
    w.append(n2)
v.insert(0,0)
w.insert(0,0)
dp = [[0] * (N+1) for i in range(M+1)]
for i in range(1,M+1):
    for j in range(1,N+1):
        if j >= v[i]:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-v[i]] + w[i])
        else :
            dp[i][j] = dp[i-1][j]
print(dp[M][N])
        