import sys

li = []

n,m = map(int,sys.stdin.readline().rstrip().split(" "))

for i in range(n):
    li.append(i+1)

for i in range(m):
    num1,num2 = sys.stdin.readline().rstrip().split(" ")
    num1 = int(num1)
    num2 = int(num2)
    many = int(num2)-int(num1) + 1
    num3 = many % 2
    num4 = int(many/2)
    if num3 == 0:
        for q in range(num4):
            tmp = li[num1+q-1]
            li[num1+q-1] = li[num2-q-1]
            li[num2-q-1] = tmp
    else :
        for q in range(num4):
            tmp = li[num1+q-1]
            li[num1+q-1] = li[num2-q-1]
            li[num2-q-1] = tmp      

for i in range(n):
    print(li[i],end=' ')