import sys

N,M = map(int,sys.stdin.readline().rstrip().split(" "))
li = []
for i in range(0,N):
    li.append(0)
for p in range(M):
    i,j,k=map(int,sys.stdin.readline().rstrip().split(" "))
    for m in range(i-1,j):
        li[m] = k

for i in range(0,N):
    print(li[i],end=' ')