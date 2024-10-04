import sys
input = sys.stdin.readline

n = int(input())
lis = []
for i in range(n):
    name,n1,n2,n3 = input().rstrip().split()
    lis.append([name,int(n1),int(n2),int(n3)])

lis.sort(key = lambda x: (-x[1],x[2],-x[3],x[0]))

for i in lis:
    print(i[0])