from collections import deque
import sys
n = int(sys.stdin.readline())
deque = deque([])
for _ in range(n):    
    lis = list(map(str,sys.stdin.readline().split()))
    if lis[0] == "push":
        deque.append(lis[1])
    elif lis[0] == "pop":
        if len(deque) == 0: print(-1)
        else: print(deque.popleft())
    elif lis[0] == "size":
        print(len(deque))
    elif lis[0] == "empty":
        if len(deque) == 0 : print(1)
        else: print(0)
    elif lis[0] == "front":
        if len(deque) == 0: print(-1)
        else : print(deque[0])
    elif lis[0] == "back":
        if len(deque) == 0: print(-1)
        else : print(deque[-1])