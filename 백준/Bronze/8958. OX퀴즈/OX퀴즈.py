t = int(input())
num2 = 0
num3 = 0
for i in range(t):
    inp = input()
    for j in range(len(inp)):
        if inp[j]=="O":
            num2 += 1
        else :
            num2 = 0
        num3 += num2
    print(num3)
    num2 = 0
    num3 = 0