import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
lis = [0] * (10001)
for _ in range(n):
    lis[int(input())] += 1

for i in range(len(lis)):
    if lis[i] != 0:
        for _ in range(lis[i]):
            print(i)