import sys

li = []
coun = 0
for i in range(10):
    li.append(0)

for i in range(10):
    num = sys.stdin.readline().rstrip()
    li[i] = int(num)%42

for i in range(0,43):
    cnt = li.count(i)
    if cnt !=0:
        coun += 1
print(coun)