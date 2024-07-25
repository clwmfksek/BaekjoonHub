n = int(input())

ch1 = 26
count = 0
for i in range(n):
    li = [False for _ in range(26)]
    ch = input()
    ch1 = ord(ch[0])-97
    li[ch1] = True
    for j in range(len(ch)):
        target = ord(ch[j])-97
        if target == ch1: continue
        else :
            if li[target]: break
            else : li[target] = True
        
        ch1 = target
    else : count += 1
print(count)