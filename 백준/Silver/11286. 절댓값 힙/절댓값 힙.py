import sys
import heapq
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

queue = []
n = int(input())

for i in range(n):
    num = int(input())
    if num :
        heapq.heappush(queue,(abs(num),num))
    else :
        if queue: print(heapq.heappop(queue)[1])
        else : print(0)