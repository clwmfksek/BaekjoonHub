import sys
inp = sys.stdin.readline
n,m = map(int,inp().split())
while(m!=0):
    tmp = m
    m = n%m
    n = tmp
print("1"*n)