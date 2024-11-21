import sys
input = sys.stdin.readline

inp1 = [""] + list(input().rstrip())
inp2 = [""] + list(input().rstrip())

lens = len(inp1)
lis = [[""] * len(inp2) for i in range(len(inp1))]

for i in range(1,len(inp1)):
    for j in range(1,len(inp2)):
        if inp1[i] == inp2[j]:
            lis[i][j] = lis[i - 1][j - 1] + inp1[i]
        else:
            if (len(lis[i-1][j]) >= len(lis[i][j-1])) : lis[i][j] = lis[i-1][j]
            else : lis[i][j] = lis[i][j-1]
print(len(lis[-1][-1]),lis[-1][-1],sep='\n')