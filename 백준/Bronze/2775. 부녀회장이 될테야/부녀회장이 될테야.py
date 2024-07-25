t = int(input())

for i in range(t):
    i = int(input())
    j = int(input())
    li = [x for x in range(1,j+1)]
    for k in range(i):
        for l in range(1,j):
            li[l] += li[l-1]
    print(li[-1])