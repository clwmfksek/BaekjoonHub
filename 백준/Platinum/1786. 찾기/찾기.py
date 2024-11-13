import sys
input = sys.stdin.readline

def failedlist(lis,lps):
    length = 0 # 매치되는 배열의 길이
    lps[0] = 0
    i = 1 
    while(i<len(lis)):
        if lis[i] == lis[length]:
            length += 1
            lps[i] = length
            i += 1
        else :
            if length == 0:
                lps[i] = 0
                i += 1
            else :
                length = lps[length-1]

t = list(input().rstrip())
p = list(input().rstrip())

lps = [0] * len(p)
failedlist(p,lps)

# 1. 배열을 전부 돌 때 까지 (i<len(t)일 동안 반복)
# 2. if t[i] == p[j] : 이면 둘이 같다는 거니까 i,j를 1씩 증가
# 3. if j가 p의 길이와 같다면(패턴이 존재한다는 것을 확인)
# 3-1. i-j(패턴이 텍스트에 존재하는 위치)를 결과 배열에 append
# 3-2. j값을 실패배열의 j-1로 바꾸기
# 4. if i가 text의 길이보다 작고, p[j] != t[i]인 경우
# 4-1. if j가 0이 아닌 경우 j값을 실패배열의 j-1로 바꾸기
# 4-2. else j가 0일 경우 i값에 1을 더해주기
i = 0
j = 0
result = []
while(i<len(t)):
    if t[i] == p[j]:
        i += 1
        j += 1
    if j == len(p):
        result.append(i-j)
        j = lps[j-1]
    elif i < len(t) and p[j] != t[i]:
        if j == 0 : i += 1
        else : j = lps[j-1]

result = [x+1 for x in result]
print(len(result))
print(*result)