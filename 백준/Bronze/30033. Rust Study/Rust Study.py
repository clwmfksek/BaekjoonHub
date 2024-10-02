n = int(input())
a = list(input().split())
b = list(input().split())

sum = 0

for i in range(n):
    if int(a[i]) <= int(b[i]):
        sum += 1
print(sum)