a = int(input(""))
b = int(input(""))

e = int(b/100)
d = int(b/10 - e*10)
c = int(b - e*100 - d*10)

print(a*c)
print(a*d)
print(a*e)
print(a*b)