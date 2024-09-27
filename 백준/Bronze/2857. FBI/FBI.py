lis = [] 
for i in range(1,6): 
    inp = input() 
    if "FBI" in inp: 
        lis.append(i) 
if lis: 
    print(*lis) 
else: 
    print("HE GOT AWAY!")