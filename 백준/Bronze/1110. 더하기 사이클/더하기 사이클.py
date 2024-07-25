n = int(input())
count = 0
num = n
while True:
    num2 = num//10
    num3 = num%10
    num4 = num2+num3
    if num<10:
        num = num+num*10
    else:
        num = num3*10 + num4%10
    count += 1
    if num == n:
        break
print(count)