from bisect import bisect_left
import sys

while(True):
    try:
        n = int(input())
        lis = list(map(int,input().split()))
        x = [lis[0]]
        for i in lis:
            if x[-1] < i:
                x.append(i)
            else:
                k = bisect_left(x,i)
                x[k] = i
        print(len(x))    
    except:
        break