import sys
input = sys.stdin.readline

s1 = list(input().rstrip())
s2 = list(input().rstrip())


while(len(s2) > len(s1)):
    if s2[-1] == "A": s2.pop()
    else :
        s2.pop()
        s2 = s2[::-1]
if s1==s2 : print(1)
else: print(0)