import sys
input = sys.stdin.readline

target = list(input().rstrip())
for i in range(len(target)):
    target[i] = int(target[i])
res1 = sum(target[:len(target)//2])
res2 = sum(target[len(target)//2:])
if res1 == res2:
    print("LUCKY")
else :
    print("READY")