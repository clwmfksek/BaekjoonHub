num = int(input())
numlist = list(map(int,input().split()))
result = 0
fir = numlist[0]
target = numlist[0]
for i in range(1,len(numlist)):
    if numlist[i] != (target+1) :
        result += fir
        fir = numlist[i]
    target = numlist[i]
result += fir
print(result)