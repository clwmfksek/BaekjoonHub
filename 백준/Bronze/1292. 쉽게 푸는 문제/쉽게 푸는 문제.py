a,b = map(int,input().split())
li = []
for i in range(b+1):
    for j in range(i):
        li.append(i)
li = li[a-1:b]
print(sum(li))