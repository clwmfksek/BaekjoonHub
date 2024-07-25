from collections import Counter

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int,input().split()))

arr3 = Counter(arr)

for i in arr2:
    if i in arr3: print(1,end=' ')
    else: print(0,end=' ')