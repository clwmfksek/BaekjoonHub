import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(node,p):
    visited[node] = p
    for i in graph[node]:
        if not visited[i]:
            a = dfs(i,-p)
            if not a:
                return False
        elif visited[i] == visited[node]:
            return False
       
    return True

for _ in range(int(input())):
    V,E = map(int,input().split())
    graph = [[] for i in range(V+1)]
    visited = [0] * (V+1)

    for i in range(E):
        s,e = map(int,input().split())
        graph[s].append(e)
        graph[e].append(s)

    for i in range(1,V+1):
        if not visited[i]:
            res = dfs(i,1)
            if not res :
                break
    
    print("YES" if res else "NO")