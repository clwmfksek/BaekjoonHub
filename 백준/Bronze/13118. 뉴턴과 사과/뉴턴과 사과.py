import sys
input = sys.stdin.readline

lis = list(map(int,input().split()))
x,y,r = map(int,input().split())

if x in lis : print(lis.index(x)+1)
else : print(0)