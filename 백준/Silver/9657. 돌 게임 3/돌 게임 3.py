import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 1001
dp[1] = 1
dp[2] = 0
dp[3] = 1
dp[4] = 1

for i in range(5,1001):
    if(not dp[i-1] or not dp[i-3] or not dp[i-4]):
        dp[i] = 1
    else :
        dp[i] = 0
        
if (dp[n]):
    print("SK");
else:
    print("CY");