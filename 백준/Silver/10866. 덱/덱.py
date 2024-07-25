import sys
input = sys.stdin.readline
N = int(input())
li = []

def pf(li, n):
    li.insert(0, n)
    return li

def pb(li, n):
    li.append(n)
    return li

def popf(li):
    if len(li) == 0:
        print(-1)
    else:
        print(li.pop(0))
    return li

def popb(li):
    if len(li) == 0:
        print(-1)
    else:
        print(li.pop())
    return li

for i in range(N):
    l = list(map(str, input().split()))
    if l[0] == "push_front":
        li = pf(li, l[1])
    elif l[0] == "push_back":
        li = pb(li, l[1])
    elif l[0] == "pop_front":
        li = popf(li)
    elif l[0] == "pop_back":
        li = popb(li)
    elif l[0] == "size":
        print(len(li))
    elif l[0] == "empty":
        if len(li) == 0:
            print(1)
        else:
            print(0)
    elif l[0] == "front":
        if len(li) == 0:
            print(-1)
        else:
            print(li[0])
    elif l[0] == "back":
        if len(li) == 0:
            print(-1)
        else:
            print(li[-1])