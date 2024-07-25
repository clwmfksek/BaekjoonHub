N = int(input())
l = list(map(str,input()))
sum = 0
for i in range(N):
    l[i] = ord(l[i])-96

for i in range(N):
    sum += l[i]*(31**i)
print(sum%1234567891)