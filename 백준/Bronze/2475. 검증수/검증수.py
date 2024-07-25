res = 0
li = list(map(int,input().split()))
for i in range(5):
    res = res + (li[i]*li[i])
print(res%10)