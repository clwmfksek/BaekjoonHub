from bisect import bisect_right

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(s1,s2):
    s1 = find(s1)
    s2 = find(s2)
    if s1 > s2:
        parent[s1] = s2
    else :
        parent[s2] = s1

n,m,k = map(int,input().split())
lis = list(map(int,input().split()))
spend = list(map(int,input().split()))

visited = [0] * (m+1)

parent = [i for i in range(n+1)]
lis.sort()
result = []
for i in spend:
    target = bisect_right(lis,i) # 만약 해당 값이 주인이 있다면 다음 값을 찾는걸 시도하지 않음.
    while(True):
        if find(lis[target]) == lis[target]:
            union(lis[target],i)
            result.append(lis[target])
            break
        else :
            target += 1
for i in result:
    print(i)