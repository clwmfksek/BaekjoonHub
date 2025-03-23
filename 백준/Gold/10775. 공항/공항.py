def find(x):
    if lis[x] != x:
        lis[x] = find(lis[x])
    return lis[x]

def union(s1,s2):
    s1 = find(s1)
    s2 = find(s2)
    if s1 > s2:
        lis[s1] = s2
    else :
        lis[s2] = s1

g = int(input())
p = int(input())

lis = [i for i in range(g+1)]
pl = []
count = 0
for i in range(p):
    pl.append(int(input()))

for i in pl:
    x = find(i)
    if x == 0:
        break
    union(x,x-1)
    count += 1
print(count)