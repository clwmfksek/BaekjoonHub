n,k =map(int,input().split())
lis = list(map(int,input().split()))

sumd = 0
target = 0
for i in range(n):
    sumd += lis[i]
    if sumd > k :
        break
    target += 1
print(target)