import sys

li = []
for i in range(1,31):
    li.append(i)

for j in range(28):
    num = sys.stdin.readline().rstrip()
    num1 = int(num) - 1
    li[num1] = 0

for k in range(30):
    if li[k] != 0:
        print(li[k])