import sys

while True:
    n1,n2=map(int,sys.stdin.readline().split())
    if n1 == 0 and n2 == 0:
        break
    else :
        print(f"{n1+n2}")