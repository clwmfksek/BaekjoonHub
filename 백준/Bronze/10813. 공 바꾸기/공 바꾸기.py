import sys

n,m = map(int,sys.stdin.readline().rstrip().split(" "))
li = []
for i in range(1,n+1):
    li.append(i)
for i in range(m):
    num1,num2 = map(int,sys.stdin.readline().rstrip().split(" "))
    tmp = li[num1-1]
    li[num1-1] = li[num2-1]
    li[num2-1] = tmp

for i in range(n):
    print(li[i],end=' ')