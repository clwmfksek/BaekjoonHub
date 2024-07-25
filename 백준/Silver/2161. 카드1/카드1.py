N = int(input())

l = [i for i in range(1,N+1)]
li = []

for i in range(N+1):
    if(len(l)!= 1):
        li.append(l.pop(0))
        l.append(l.pop(0))
li.append(l[0])
for i in li:
    print(i,end=' ')