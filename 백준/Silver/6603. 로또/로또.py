import sys
input = sys.stdin.readline

def bt(start):
    if len(result)==6:
        print(*result)
        return
    remember = 0
    for i in range(start,num):
        if visited[i] == 0 and remember != lis[i] and lis[i] > remember:
            result.append(lis[i])
            remember = lis[i]
            visited[i] = 1
            bt(i+1)
            result.pop()
            visited[i] = 0
while(True):
    lis = list(map(int,input().split()))
    num = lis[0]
    if num == 0:
        break
    lis = lis[1:]
    result = []
    visited = [0] * (num+1)
    bt(0)
    print()
