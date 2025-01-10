from collections import Counter
import sys
input = sys.stdin.readline

for i in range(3):
    lis = [*map(int,input().split())]
    c = Counter(lis)
    if c[0] == 4 : print("D")
    elif c[0] == 3 : print("C")
    elif c[0] == 2 : print("B")
    elif c[0] == 1 : print("A")
    elif c[0] == 0 : print("E")