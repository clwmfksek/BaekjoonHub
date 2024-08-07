import sys
input = sys.stdin.readline

def init(start, end, node):
    if start == end:
        seg_tree[node] = nums[start]
        return seg_tree[node]
    mid = (start + end) // 2
    seg_tree[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2 + 1)
    return seg_tree[node]

def update(node, start, end, idx, val):
    if start == end:
        seg_tree[node] = val
        return
    mid = (start + end) // 2
    if start <= idx <= mid:
        update(node * 2, start, mid, idx, val)
    else:
        update(node * 2 + 1, mid + 1, end, idx, val)
    seg_tree[node] = seg_tree[node * 2] + seg_tree[node * 2 + 1]

def query(left, right, node, start, end):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return seg_tree[node]
    mid = (start + end) // 2
    return query(left, right, node * 2, start, mid) + query(left, right, node * 2 + 1, mid + 1, end)

nums = []
N, M, K = map(int, input().split())
for _ in range(N):
    nums.append(int(input()))

seg_tree = [0] * (4 * N)
init(0, N - 1, 1)

for _ in range(M + K):
    n1, n2, n3 = map(int, input().split())
    if n1 == 1:
        update(1, 0, N - 1, n2 - 1, n3)
    else:
        print(query(n2 - 1, n3 - 1, 1, 0, N - 1)) 