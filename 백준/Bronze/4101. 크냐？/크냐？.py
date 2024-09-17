while True:
    n1,n2 = map(int,input().split())
    if n1 == n2 == 0: break
    else :
        print("Yes" if n1 > n2 else "No")