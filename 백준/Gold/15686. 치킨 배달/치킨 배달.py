import sys
input = sys.stdin.readline
from itertools import combinations

n,m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

chouse = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chouse.append([i,j])

chouses = list(combinations(chouse,m))

result = sys.maxsize

for k in chouses:
    var = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                count = sys.maxsize
                for l in k:
                    count = min(count,abs(i-l[0]) + abs(j-l[1]))
                var += count
    result = min(result,var)

print(result)