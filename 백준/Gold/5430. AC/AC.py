import sys
input = sys.stdin.readline
from collections import deque

t = int(input())

for i in range(t):
    func = list(input().rstrip())
    n = int(input())
    nums = list(input().rstrip())
    prev = ""
    num = deque([])
    for i in nums:
        if i.isalnum(): prev += i
        elif i == "[" : continue
        elif i == "]" :
            if prev == "" : continue
            else : num.append(int(prev))
        else : 
            num.append(int(prev))
            prev = ""
    bol = True
    rev = False
    for i in func:
        if i == "D":
            if num:
                if rev:
                    num.pop()
                else :
                    num.popleft()
            else :
                bol = False
                break
        else :
            if rev : rev = False
            else : rev = True
    num = list(num)
    if rev : num.reverse()

    if bol : print("[" + ','.join(map(str,num)) + "]")
    else : print("error")