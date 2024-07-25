import sys
l =[]
ma = 0
m = 0
for i in range(9):
    l.append(int(sys.stdin.readline()))
    if l[i] > ma:
        ma = l[i]
        m = i+1
print(ma)
print(m)