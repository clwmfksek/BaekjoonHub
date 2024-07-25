def rev(x):
    return int(str(x)[::-1])

n,m = map(int,input().split())

print(rev(rev(n)+rev(m)))