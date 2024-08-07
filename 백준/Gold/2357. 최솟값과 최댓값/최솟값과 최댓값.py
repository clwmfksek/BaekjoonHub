import sys
input = sys.stdin.readline

def init(start, end, node):
    if start == end:
        seg_tree[node] = (lis[start], lis[start])
        return seg_tree[node]
    mid = (start + end) // 2
    leftchild = init(start, mid, node * 2)
    rightchild = init(mid + 1, end, node * 2 + 1)
    seg_tree[node] = (min(leftchild[0], rightchild[0]), max(leftchild[1], rightchild[1]))
    return seg_tree[node]

def query(left, right, node, start, end):
    if left > end or right < start:
        return (1e9+1, 0)
    if left <= start and end <= right:
        return seg_tree[node]
    mid = (start + end) // 2
    leftchild = query(left, right, node * 2, start, mid)
    rightchild = query(left, right, node * 2 + 1, mid + 1, end)
    return (min(leftchild[0], rightchild[0]), max(leftchild[1], rightchild[1]))

N, M = map(int, input().split())
lis = []
seg_tree = [(1e9, 0)] * (N * 4)
for _ in range(N):
    lis.append(int(input()))

init(0, N - 1, 1)
for _ in range(M):
    n1, n2 = map(int, input().split())
    print(*query(n1 - 1, n2 - 1, 1, 0, N - 1))
