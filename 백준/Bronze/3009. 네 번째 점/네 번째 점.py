import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())

for i in [x1,x2,x3]:
    if [x1,x2,x3].count(i) == 1 : x4 = i
for i in [y1,y2,y3]:
    if [y1,y2,y3].count(i) == 1 : y4 = i
print(x4,y4)