import sys
n = int(sys.stdin.readline())
li = []
for i in range(n): li.append(sys.stdin.readline())
li = set(li)
li = list(li)
li.sort()
li.sort(key=len)
for i in li:
    print(i,end='')