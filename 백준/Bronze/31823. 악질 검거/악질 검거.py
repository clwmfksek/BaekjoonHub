N, M = map(int, input().split())
countStreak = set()
KPSC_List = []

for _ in range(N):
    record = input().split()
    streak, name = record[:M], record[M]

    result = 0  
    count = 0
    for i in streak:
        if i == ".": count += 1  
        else: count = 0  
        result = max(result, count)  

    countStreak.add(result) 
    KPSC_List.append([result, name])  

print(len(countStreak))
for K in KPSC_List:
    print(*K)