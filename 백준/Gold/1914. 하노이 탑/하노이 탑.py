import sys
input = sys.stdin.readline

def hanoi(n,start,temp,to):
    if n == 1 :
        print(start,to)
        return
    
    hanoi(n-1,start,to,temp)
    print(start,to)
    hanoi(n-1,temp,start,to)

n = int(input())
if n == 1 : 
    print(1)
    hanoi(n,1,2,3)
else:
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 3
    for i in range(3,n+1):
        dp[i] = 2*dp[i-1] + 1
    print(dp[n])
    if n <= 20 :
        hanoi(n,1,2,3)