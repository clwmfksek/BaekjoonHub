n = int(input())
test_list = list(map(int,input().split()))
num = max(test_list)

new_list = []
for score in test_list :
    new_list.append(score/num *100)
print(sum(new_list)/n)
