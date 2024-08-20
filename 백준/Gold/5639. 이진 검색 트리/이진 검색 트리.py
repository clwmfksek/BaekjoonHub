import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

a = []

while True:
    try:
        a.append(int(input()))
    except:
        break

def find(start,end):
    if start > end :
        return

    finder = end+1
    s = a[start]
    for i in range(start+1,end+1):
        if a[i] > s :
            finder = i
            break
    find(start+1,finder-1)
    find(finder,end)
    print(a[start])
    


find(0,len(a)-1)