a,b,c = map(int,input().split())
print((a+b+c)//3 + (0 if (a%3==b%3==c%3) else 1))