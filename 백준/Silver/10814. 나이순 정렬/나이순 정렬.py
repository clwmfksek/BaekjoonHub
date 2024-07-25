n = int(input())

lis = []

for i in range(n):
    age,name = map(str,input().split())
    age = int(age)
    lis.append([age,name])
lis.sort(key = lambda x: x[0])
for i in lis:
    print(i[0],i[1])