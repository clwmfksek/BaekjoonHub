
res = []
for i in range(9):
    res.append(list(map(int,input().split())))
maxnum = 0
row = 0
col = 0
for i in range(9):
    for j in range(9):
        if maxnum <= res[i][j]:
            row = i+1
            col = j+1
            maxnum = res[i][j]
print(maxnum)
print(row,col)