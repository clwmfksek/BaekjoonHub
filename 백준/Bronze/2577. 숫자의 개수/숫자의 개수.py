a = int(input())
b = int(input())
c = int(input())

res = str(a*b*c)
li = [i for i in range(10)]

for i in range(10):
    print(res.count(str(i)))