import sys

input=sys.stdin.readline
sys.setrecursionlimit(10**6)

n,k=map(int,input().split())
lis = list(map(int,input().split()))

start= end = 0
sumd=0
count = 1e9

def minn(num1,num2):
    if num1 > num2 :
        return num2
    else : return num1

while True:
    if sumd >= k:
        count = minn(count,end-start)
        sumd -= lis[start]
        start += 1
    elif end == n:
        break
    else :    
        sumd+=lis[end]
        end += 1
if count == 1e9:
    print(0)
else:
    print(count)