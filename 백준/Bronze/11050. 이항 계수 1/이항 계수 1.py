def factorial(num1):
    if (num1>1): 
        return factorial(num1-1) * num1
    else: 
        return 1

l = list(map(int,input().split()))
print(int(factorial(l[0])/(factorial(l[1])*factorial(l[0]-l[1]))))