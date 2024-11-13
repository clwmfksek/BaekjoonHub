def fail(t):
    lent = len(t)
    ls = [0] * lent
    i = 1
    length = 0
    while i < lent:
        if t[i] == t[length]:  # 두 문자가 같다면
            length += 1
            ls[i] = length
            i += 1
        else:
            if length == 0:
                ls[i] = 0
                i += 1
            else:
                length = ls[length - 1]
    return ls

while True:
    t = input()
    if t == ".":
        break
    else:
        lps = fail(t)
        n = len(t)
        longest_prefix_suffix = lps[-1]  # LPS 배열의 마지막 값

        # 문자열이 반복되는 패턴을 가지는지 확인
        if n % (n - longest_prefix_suffix) == 0:
            maxnum = n // (n - longest_prefix_suffix)
        else:
            maxnum = 1

        print(maxnum)