import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    lis = list(map(int, input().split()))
    
    maxvalue = 0
    gain = 0
    
    for i in range(n - 1, -1, -1):
        if lis[i] > maxvalue:
            maxvalue = lis[i]
        else:
            gain += maxvalue - lis[i]
    
    print(gain)
