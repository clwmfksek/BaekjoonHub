inp = list(input().split(" "))
count = 0
for i in range(len(inp)):
    if inp[i] != '':
        count += 1
print(count)