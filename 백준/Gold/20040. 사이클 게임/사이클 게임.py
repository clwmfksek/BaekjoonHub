n,m = map(int,input().split())

graph = [i for i in range(n)]

def find(x):
    while x!= graph[x]:
        x = graph[x]
    return x

def union(s1,s2):
    s1 = find(s1)
    s2 = find(s2)
    if s1 < s2 :
        graph[s2] = s1
    else :
        graph[s1] = s2
count = 0
for _ in range(1,m+1):
    a,b = map(int,input().split())
    s1 = find(a)
    s2 = find(b)
    if s1 == s2:
        count = _
        break
    union(s1,s2)
print(count)