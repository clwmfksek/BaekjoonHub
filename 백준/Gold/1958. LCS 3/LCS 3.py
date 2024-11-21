import sys
input = sys.stdin.readline

inp1 = input().rstrip()
inp2 = input().rstrip()
inp3 = input().rstrip()

def lcs3(a, b, c):
    len_a, len_b, len_c = len(a), len(b), len(c)
    dp = [[[0]*(len_c+1) for _ in range(len_b+1)] for __ in range(len_a+1)]

    for i in range(1, len_a+1):
        for j in range(1, len_b+1):
            for k in range(1, len_c+1):
                if a[i-1] == b[j-1] == c[k-1]:
                    dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                else:
                    dp[i][j][k] = max(
                        dp[i-1][j][k],
                        dp[i][j-1][k],
                        dp[i][j][k-1]
                    )
    return dp[len_a][len_b][len_c]

print(lcs3(inp1, inp2, inp3))