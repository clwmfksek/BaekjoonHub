lis = []
while True:
    try:
        lis.append(int(input()))
    except : break
print(sum(lis))