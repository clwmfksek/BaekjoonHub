n = input()
for i in range(1,len(n)//10+2):
    if (i-1)*10 < 0:
        print(n[0:i*10])
    elif(i*10 > len(n)) :
        print(n[(i-1)*10:])
    else :
        print(n[(i-1)*10 : i*10])