import sys
input = sys.stdin.readline
a = [0] * 10

end = int(input())

p = 1
s = 1

def cal(x,a,p):
    while x > 0:
        a[x % 10] += p
        x //= 10
        

while s <= end:
    while end % 10 != 9:
        cal(end, a, p)
        end -= 1
    if end < s:
        break
    while s % 10 != 0:
        cal(s, a, p)
        s += 1
    s //= 10
    end //= 10
    for i in range(10):
        a[i] += (end - s + 1) * p
    p *= 10

print(*a)
# 참고