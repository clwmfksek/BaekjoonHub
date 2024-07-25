l = input()
li = []
for i in range(len(l)):
    li.append(l[i:len(l)])
li.sort()
for i in li:
    print(i)
