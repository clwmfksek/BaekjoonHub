li = []
for i in range(97,123):
    li.append(-1)
n = input()
for i in range(len(n)) :
    for j in range(97,123):
        if li[j-97] == -1 :
            if chr(j) == n[i]:
                li[j-97] = i
for i in range(97,123):
    print(li[i-97],end=' ')