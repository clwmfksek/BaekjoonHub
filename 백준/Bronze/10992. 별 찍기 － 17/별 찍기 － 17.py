n = int(input())
for i in range(1,n+1):
    print(" "*(n-i),end='')
    if i==n:
        print("*"*(2*i-1))
    elif i==1:
        print("*")
    else:
        print("*"+" "*(2*i-3)+"*")