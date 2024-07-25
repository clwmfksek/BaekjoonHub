import sys
n = int(sys.stdin.readline())
l = [sys.stdin.readline().split()]
n1 = int(sys.stdin.readline())
c = 0
for i in l[0]:
    if int(i) == n1 : c+=1
print(c)