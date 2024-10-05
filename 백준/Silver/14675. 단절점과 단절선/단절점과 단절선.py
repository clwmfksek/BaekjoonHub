import sys
input = sys.stdin.readline

n = int(input())

tree = [0 for i in range(n+1)]
for i in range(n-1):
    n1,n2 = map(int,input().split())
    tree[n1] += 1
    tree[n2] += 1

m = int(input())

for i in range(m):
    n1,n2 = map(int,input().split())
    if n1 == 1:
        if tree[n2] == 1 : print("no")
        else : print("yes")
    else : print("yes")