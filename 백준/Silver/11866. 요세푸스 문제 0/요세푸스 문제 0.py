n,m = map(int,input().split())

arr2 = []
arr = [i for i in range(1,n+1)]

target = 0

for _ in range(n):
    target += m-1
    if target >= len(arr):
        target = target % len(arr)
    arr2.append(arr.pop(target))
print("<"+str(arr2).lstrip("[").rstrip("]")+">")