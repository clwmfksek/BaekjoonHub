a,b = map(int,input().split(" "))
count = 0
m = 0
for i in range(1,a+1):
    if a%i == 0 : count += 1
    if b == count : 
        m = i
        break
print(m)