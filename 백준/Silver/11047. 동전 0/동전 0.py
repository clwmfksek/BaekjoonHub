n,k = map(int,input().split())
li = []
count = 0
for i in range(n):
    li.append(int(input()))

for i in li[::-1]:
    count += k//i
    k = k%i
    if(k==0): break

print(count)