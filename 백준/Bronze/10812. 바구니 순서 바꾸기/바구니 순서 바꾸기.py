import sys
input = sys.stdin.readline

n,m = map(int,input().split())

lis = [i for i in range(1,n+1)]

for i in range(m):
    n1,n2,n3 = map(int,input().split())
    n1 -= 1
    n2 -= 1
    n3 -= 1
    lis = lis[:n1] + lis[n3:n2+1] + lis[n1:n3]+ lis[n2+1:]
print(*lis)