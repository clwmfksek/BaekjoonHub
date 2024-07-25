import sys
n = int(sys.stdin.readline())

for i in range(1,n+1):
    n1,n2=map(int,sys.stdin.readline().split())
    print(f"Case #{i}: {n1+n2}")