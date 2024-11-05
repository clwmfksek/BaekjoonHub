import sys
import heapq
input = sys.stdin.readline

n = int(input())
lis = [list(map(int,input().split())) for i in range(n)]

lis.sort()
heap = []
for i in lis:
    if heap:
        hpop = heapq.heappop(heap)
        if hpop <= i[0]:
            heapq.heappush(heap,i[1])
        else :
            heapq.heappush(heap,hpop)
            heapq.heappush(heap,i[1])
    else :
        heapq.heappush(heap,i[1])
print(len(heap))