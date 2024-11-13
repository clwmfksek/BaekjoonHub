t = input()

def fail(t):
    lent = len(t)
    ls = [0] * lent
    i = 1
    length = 0
    while(i<lent):
        if t[i] == t[length]: # 두 문자가 같다면
            length += 1 # 일치하는 문자열의 길이를 1을 늘려주고
            ls[i] = length # ls의 i번째를 문자열의 길이로 설정
            i += 1 # 다음 인덱스 탐지
        else :
            if length == 0 : # 만약 일치하는 문자열의 길이가 0이라면
                ls[i] = 0 # i번째 실패배열을 0으로 설정
                i += 1 # 다음 인덱스 탐지
            else : # 일치하는 문자열이 0 초과라면
                length = ls[length-1] # length의 값을 실패 배열의 length-1값으로 설정
    return ls
ans = 0
for i in range(len(t)):
    ans = max(ans,max(fail(t[i:])))
print(ans)