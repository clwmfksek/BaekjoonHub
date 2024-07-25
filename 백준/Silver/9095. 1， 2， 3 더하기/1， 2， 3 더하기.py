t = int(input())
count = 0
def ottplus(inp):
    if inp == 0:
        return 1
    if inp < 0:
        return 0
    return ottplus(inp - 1) + ottplus(inp - 2) + ottplus(inp - 3)

for _ in range(t):
    inp = int(input())
    count = ottplus(inp)
    print(count)
