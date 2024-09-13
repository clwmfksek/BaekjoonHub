import sys
input = sys.stdin.readline
idx = 1 
while True:
    L, R = map(int, input().rstrip().split())
    if L == R == 0:
        break
    else:
        o = L
        w = R
        while True:
            command, num = input().rstrip().split()
            num = int(num)
            if command == '#' and num == 0:
                if w > o / 2 and w < o * 2:
                    print(f'{idx} :-)')
                elif w <= 0:
                    print(f'{idx} RIP')
                else:
                    print(f'{idx} :-(')
                idx += 1
                break
            elif command == 'E' and w > 0:
                w -= num
            elif command == 'F' and w > 0:
                w += num

    