import sys
input = sys.stdin.readline

def init(start, end, node):
    if start == end:
        if nums[start] % 2 == 0:
            seg_tree[node] = [1, 0]
        else:
            seg_tree[node] = [0, 1]
        return seg_tree[node]
    
    mid = (start + end) // 2
    left = init(start, mid, node * 2)
    right = init(mid + 1, end, node * 2 + 1)
    seg_tree[node] = [left[0] + right[0], left[1] + right[1]]
    return seg_tree[node]

def update(start, end, node, idx, val):
    if start == end:
        if val % 2 == 0:
            seg_tree[node] = [1, 0]
        else:
            seg_tree[node] = [0, 1]
        return
    
    mid = (start + end) // 2
    if idx <= mid:
        update(start, mid, node * 2, idx, val)
    else:
        update(mid + 1, end, node * 2 + 1, idx, val)
    
    seg_tree[node] = [seg_tree[node * 2][0] + seg_tree[node * 2 + 1][0], 
                      seg_tree[node * 2][1] + seg_tree[node * 2 + 1][1]]

def query(start, end, node, left, right):
    if left > end or right < start:
        return [0, 0]
    
    if left <= start and end <= right:
        return seg_tree[node]
    
    mid = (start + end) // 2
    leftm = query(start, mid, node * 2, left, right)
    rightm = query(mid + 1, end, node * 2 + 1, left, right)
    return [leftm[0] + rightm[0], leftm[1] + rightm[1]]

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
seg_tree = [0] * (n * 4)
init(0, n - 1, 1)

for _ in range(m):
    n1, n2, n3 = map(int, input().split())
    if n1 == 1:
        update(0, n - 1, 1, n2 - 1, n3)
    elif n1 == 2:
        result = query(0, n - 1, 1, n2 - 1, n3 - 1)
        print(result[0])
    else:
        result = query(0, n - 1, 1, n2 - 1, n3 - 1)
        print(result[1])
