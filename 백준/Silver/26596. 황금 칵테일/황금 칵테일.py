import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import math

dic = {}
n = int(input())

for i in range(n):
    st,num = map(str,input().rstrip().split())
    num = int(num)
    if dic.get(st) != None:
        dic[st] = dic.get(st) + num
    else :
        dic[st] = num


se = set(dic.keys())
a = []

for i in se:
    a.append(dic[i])
bol = False

for i in range(len(a)):
    for j in range(len(a)):
        if i == j : continue
        if (math.floor(a[i]*1.618) == a[j]):
            bol = True

if bol : print("Delicious!")
else : print("Not Delicious...")