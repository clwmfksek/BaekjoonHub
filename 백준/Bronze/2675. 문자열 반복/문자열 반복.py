n1 = int(input())
for i in range(n1):
    li =''
    n,inp = input().split(" ")
    n = int(n)
    for j in inp:
        li += j*n
    print(li)