import sys
n = int(sys.stdin.readline())
l = [sys.stdin.readline().rstrip().split()]
max = l[0][0]
min = l[0][0]

for i in range(n):
    if int(l[0][i]) > int(max) : max = l[0][i]
    elif int(l[0][i]) < int(min) : min = l[0][i]

print(f"{int(min)} {int(max)}")