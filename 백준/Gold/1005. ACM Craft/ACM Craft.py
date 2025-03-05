import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    n,k = map(int,input().split())
    
    # 가중치
    plus = [0] + list(map(int,input().split()))

    # indegree
    indegree = [0] * (n+1)

    # graph
    graph = [[] for i in range(n+1)]
    
    # queue
    queue = deque()

    # result
    result = [0 for i in range(n+1)]

    for i in range(k):
        n1,n2 = map(int,input().split())
        graph[n1].append(n2)
        indegree[n2] += 1
    
    # 승리하기 위해 건설해야할 건물
    win = int(input())

    for i in range(1,n+1):
        if indegree[i] == 0:
            queue.append(i)
            result[i] += plus[i]
    
    while(queue):
        target = queue.popleft() # indegree가 0인 노드
        for i in graph[target]:
            indegree[i] -= 1
            result[i] = max(result[i], result[target] + plus[i])
            if indegree[i] == 0:
                queue.append(i)
        
    print(result[win])