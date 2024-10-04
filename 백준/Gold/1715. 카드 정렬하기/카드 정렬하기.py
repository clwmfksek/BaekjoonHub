import sys
input = sys.stdin.readline
import heapq

n = int(input())
heap = []
lis = [heapq.heappush(heap,int(input())) for i in range(n)]
result = 0

while(len(heap) != 1):
    n1 = heapq.heappop(heap)
    n2 = heapq.heappop(heap)
    heapq.heappush(heap,n1+n2)
    result += n1+n2
print(result)