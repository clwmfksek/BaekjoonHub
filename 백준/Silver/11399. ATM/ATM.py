n = int(input())
li = list(map(int,input().split()))
li.sort()
l = []
result = 0
for i in li:
    result += i
    l.append(result)
print(sum(l))