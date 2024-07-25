n = int(input())
li = [n for _ in range(n+1)]
li[n] = 0
for i in range(n,0,-1):
    li[i-1] = min(li[i-1],li[i]+1)
    if (i%2==0):
        li[i//2] = min(li[i//2],li[i]+1)
    if (i%3==0):
        li[i//3] = min(li[i//3],li[i]+1)
print(li[1])