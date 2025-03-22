def find(x):
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]

def union(n1,n2):
    n1 = find(n1)
    n2 = find(n2)
    if n1 < n2 :
        parent[n1] = n2
    else :
        parent[n2] = n1

n = int(input())
m = int(input())
lis = [0]
parent = [i for i in range(n+1)]
for i in range(n):
    lis.append([0] + list(map(int,input().split())))

for i in range(1,n):
    for j in range(i+1,n+1):
        if lis[i][j] == 1 : union(i,j)

target = list(map(int,input().split()))

bol = True
for i in target:
    if find(i) != find(target[0]):
        bol = False
        break
if bol : print("YES")
else : print("NO")
