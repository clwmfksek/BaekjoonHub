n = int(input())
c = 0
l = list(map(int,input().split()))
for i in range(n):
    count = 0
    for j in range(1,l[i]+1):
        if l[i] % j == 0:
            count += 1
    if count == 2 :
        c += 1
print(c)