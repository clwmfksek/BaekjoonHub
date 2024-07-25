def fac(num):
    if num>1: return num * fac(num-1)
    else : return 1
n = int(input())
count = 0
num = str(fac(n))
for i in range(len(num)):
    if num[len(num)-i-1] == "0":
        count += 1
    else : break
print(count)