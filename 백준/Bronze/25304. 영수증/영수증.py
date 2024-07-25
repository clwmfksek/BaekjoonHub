x = int(input())
y = int(input())
sum = 0
for i in range(y):
    a,b = map(int,input().split(" "))
    sum += a*b
if sum == x : print("Yes")
else : print("No")