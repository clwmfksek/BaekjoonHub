import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a,k = map(int,input().split())
li = list(map(int,input().split()))
count = 0

def ssort(li):
    global count
    for last in range(len(li),1,-1):
        ma = max(li[:last])
        if (ma != li[last-1]):
            temp = li[li.index(ma)]
            li[li.index(ma)] = li[last-1]
            li[last-1] = temp
            count += 1
            if count == k:
                for i in li:
                    print(i,end=' ')
                return
    if count < k :
        print(-1)
ssort(li)