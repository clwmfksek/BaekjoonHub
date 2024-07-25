l = list(map(int,input()))
if sum(l) % 3 == 0 and 0 in l:
    l.sort(reverse=True)
    for i in l:
        print(i,end='')
else:
    print(-1)