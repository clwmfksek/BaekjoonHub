import sys
input = sys.stdin.readline
n = int(input())

if n == 1:
    print('CY')
elif n == 2:
    print('SK')
elif n == 3:
    print('CY')
elif n == 4:
    print('SK')
else:
    dp = [-1] * (n+1)
    dp[1] = 'CY'
    dp[2] = 'SK'
    dp[3] = 'CY'
    dp[4] = 'SK'

    for i in range(5, n+1):
        if dp[i-1] == 'CY' or dp[i-3] == 'CY' or dp[i-4] == 'CY':
            dp[i] = 'SK'
        else:
            dp[i] = 'CY'
    print(dp[n])