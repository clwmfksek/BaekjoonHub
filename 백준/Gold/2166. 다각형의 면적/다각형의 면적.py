import sys
input = sys.stdin.readline

n = int(input())
x,y = [],[]
for i in range(n):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)
result = 0
x.append(x[0])
y.append(y[0])
dx = 0
dy = 0
for i in range(n):
    dx += x[i] * y[i+1]
    dy += y[i] * x[i+1]
print(round(float(abs(dx-dy)/2),1))