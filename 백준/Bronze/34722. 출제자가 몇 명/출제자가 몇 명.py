count = 0
for _ in range(int(input())):
    b,c,a,i = map(int,input().split())
    if b >= 1000 or c >= 1600 or a >= 1500 or 1 <= i <= 30 : count += 1
print(count)