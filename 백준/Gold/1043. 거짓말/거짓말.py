import sys
input = sys.stdin.readline

def find(x):
    if(x==parent[x]):
        return x
    return find(parent[x])

def union(x,y):
    x = find(x)
    y = find(y)
    if x != y :
        parent[x] = y

n,m = map(int,input().split())
parent = [0] * (n+1)
parties = []
lier = set(list(map(int,input().split()))[1:])
for i in range(m):
    party = set(list(map(int,input().split()))[1:])
    parties.append(party)
for _ in range(m):
    for party in parties:
         if lier & party:
            lier = lier.union(party)

count = 0
for p in parties:
    if lier.intersection(p):
        continue
    count += 1
print(count)