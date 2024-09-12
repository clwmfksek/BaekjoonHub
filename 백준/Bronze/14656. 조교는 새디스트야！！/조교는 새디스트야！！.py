import sys
input = sys.stdin.readline
n = int(input())
lis = list(map(int,input().split()))
lis2 = sorted(lis)
count = 0
for i in range(len(lis)):
    if lis[i] != lis2[i]: count += 1

print(count)