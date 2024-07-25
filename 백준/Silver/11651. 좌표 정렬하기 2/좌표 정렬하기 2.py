n = int(input())
li = []
for i in range(n):
    num1,num2 = map(int,input().split())
    li.append((num1,num2))

li.sort(key=lambda x:(x[1],x[0]))
for i in li:
    print(i[0], i[1])