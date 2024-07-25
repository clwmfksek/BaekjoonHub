import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

name, prefer, distance = input().rstrip().split()
distance = int(distance)
prefer = sorted(list(prefer))
n = int(input())
people = []

for i in range(n):
    fname, fprefer, fdistance = input().rstrip().split()
    fprefer = sorted(list(fprefer))
    fdistance = int(fdistance)
    
    if fdistance <= distance:
        if any(p in fprefer for p in prefer): 
            people.append(fname)

if len(people) == 0:
    print("No one yet")
else:
    people.sort()
    for i in people:
        print(i)
