import sys
input = sys.stdin.readline
n = int(input())
lis = list(map(int,input().split()))

result = []
for i in range(n):
    result.insert(len(result)-lis[i],i+1)
print(*result)