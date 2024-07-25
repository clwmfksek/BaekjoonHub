di = {}
ma = 0
man = 0

for i in range(65,91):
    di[chr(i)] = 0

inp = list(input())

for i in inp:
    di[i.upper()] += 1

for i in range(65,91):
    if ma < di[chr(i)]:
        ma = di[chr(i)]
        man = chr(i)
    elif ma == di[chr(i)]:
        man = "?"

print(man)