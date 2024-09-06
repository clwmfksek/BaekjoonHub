import sys
input = sys.stdin.readline

target = list(input().rstrip())
count = 0
for i in range(len(target)-1):
    if target[i+1] != target[i]:
        count += 1
print((count+1)//2)