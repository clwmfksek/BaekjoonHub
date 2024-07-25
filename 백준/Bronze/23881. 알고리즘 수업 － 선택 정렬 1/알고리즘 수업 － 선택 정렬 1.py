a,k = map(int,input().split())
li = list(map(int,input().split()))
count = 0
def ssort(li):
    global count
    for last in range(len(li),1,-1):
        ma = max(li[:last])
        if (ma != li[last-1]):
            num = li[last-1]
            temp = li[li.index(ma)]
            li[li.index(ma)] = li[last-1]
            li[last-1] = temp
            count += 1
            if count == k:
                print(num,temp)
                return
    if count < k :
        print(-1)
ssort(li)