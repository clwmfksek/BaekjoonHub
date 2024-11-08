import sys
input = sys.stdin.readline

n,m = map(int,input().split())

f1 = m%10
f2 = (2*m)%10

lis = []
for i in range(1,n+1):
    x = i % 10
    if f1 != x and f2 != x:
        lis.append(i)
print(len(lis))
print(*lis)