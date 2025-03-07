import sys
input = sys.stdin.readline

def find(x):
    if graph[x] != x:
        graph[x] = find(graph[x])
    return graph[x]

def union(s1,s2):
    s1 = find(s1)
    s2 = find(s2)
    if s1 < s2 :
        graph[s1] = s2
    else :
        graph[s2] = s1

for i in range(int(input())):
    n = int(input())
    graph = [j for j in range(n)]

    for j in range(int(input())):
        n1,n2 = map(int,input().split())
        union(n1,n2)

    print(f"Scenario {i+1}:")

    for j in range(int(input())):
        n1,n2 = map(int,input().split())
        if(find(n1)==find(n2)) : print(1)
        else : print(0)
    print()
    