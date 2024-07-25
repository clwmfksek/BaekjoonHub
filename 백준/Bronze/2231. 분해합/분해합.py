N = int(input())
num1 = 0
for i in range(N):
    num = i
    l = list(map(int,str(i)))
    for j in l:
        num += j
    if num == N:
        num1 = i
        break
print(num1)