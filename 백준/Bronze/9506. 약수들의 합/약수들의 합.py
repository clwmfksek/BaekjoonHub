n = 0

while True:
    li = []
    n = int(input())
    if n == -1 : break
    for i in range(1,n):
        if n%i==0:
            li.append(i)
    if sum(li) == n:
        print(f"{i+1} = ",end='')
        for j in li:
            if j==min(li):
                print(j,end='')
            else :
                print(f" + {j}",end='')
        print("")
    else :
        print(f"{i+1} is NOT perfect.")