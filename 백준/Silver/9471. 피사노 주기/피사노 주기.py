import sys
input = sys.stdin.readline

def sol(num):
    ans = 1
    m1,m2 = 1,2
    while True:
        if m1%num == 1 and m2%num == 1:
            break
        ans += 1
        m1,m2 = m2,(m1+m2)%num
    return ans

t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    ans = sol(m)
    print(f"{n} {ans}")