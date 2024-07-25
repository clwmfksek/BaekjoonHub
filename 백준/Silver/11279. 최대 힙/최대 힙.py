import sys
import heapq
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
t = int(input())
hep = []

for _ in range(t):
    num = int(input())
    if num == 0:
        if not hep:
            print(0)
        else:
            print(heapq.heappop(hep)[1])
    else :
        heapq.heappush(hep,(-num,num))