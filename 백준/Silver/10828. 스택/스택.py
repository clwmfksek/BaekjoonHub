import sys
input = sys.stdin.readline
N = int(input())
li = []
def push(x,lo):
    lo[len(lo):] = [x]
    return lo

def pop(lo):
    if len(lo) == 0:
        print(-1)
    else:
        print(lo[len(lo)-1])
        del lo[len(lo)-1]
    return lo

def size(lo):
    print(len(lo))

def empty(lo):
    if len(lo) == 0:
        print(1)
    else:
        print(0)

def top(lo):
    if len(lo) == 0:
        print(-1)
    else:
        print(lo[len(lo)-1])

for i in range(N):
    l=list(map(str,input().split()))
    if l[0] == 'push':
        l = push(l[1],li)
    elif l[0] == 'pop':
        l=pop(li)
    elif l[0] == 'size':
        size(li)
    elif l[0] == 'empty':
        empty(li)
    elif l[0] == 'top':
        top(li)