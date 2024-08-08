import sys
input = sys.stdin.readline

def pmz(num):
    if num > 0: return 1
    elif num < 0: return -1
    else: return 0

def init(start, end, node):
    if start == end:
        seg_tree[node] = pmz(nums[start])
        return seg_tree[node]
    mid = (start + end) // 2
    seg_tree[node] = init(start, mid, node * 2) * init(mid + 1, end, node * 2 + 1)
    return seg_tree[node]

def query(left, right, node, start, end):
    if left > end or right < start: return 1
    if left <= start and end <= right: return seg_tree[node]
    mid = (start + end) // 2
    return query(left, right, node * 2, start, mid) * query(left, right, node * 2 + 1, mid + 1, end)

def update(start, end, node, ind, val):
    if start == end:
        seg_tree[node] = val
        return
    mid = (start + end) // 2
    if ind <= mid:
        update(start, mid, node * 2, ind, val)
    else:
        update(mid + 1, end, node * 2 + 1, ind, val)
    seg_tree[node] = seg_tree[node * 2] * seg_tree[node * 2 + 1]

try:
    while True:
        line = input()
        if not line:
            break

        N, K = map(int, line.split())
        nums = list(map(int, input().split()))
        seg_tree = [0] * (N * 4)

        init(0, N - 1, 1)
        result = []

        for _ in range(K):
            cmd = input().split()
            n1, n2, n3 = cmd[0], int(cmd[1]), int(cmd[2])

            if n1 == 'P':
                res = query(n2 - 1, n3 - 1, 1, 0, N - 1)
                if res == 0:
                    result.append('0')
                elif res > 0:
                    result.append('+')
                else:
                    result.append('-')
            else:
                update(0, N - 1, 1, n2 - 1, pmz(n3))

        print("".join(result))
except Exception as e:
    pass
