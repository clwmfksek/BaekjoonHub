import sys
input = sys.stdin.readline

def init(start, end, node):
    if start == end:
        seg_tree[node] = lis[start]
        return seg_tree[node]
    mid = (start + end) // 2
    leftchild = init(start, mid, node * 2)
    rightchild = init(mid + 1, end, node * 2 + 1)
    seg_tree[node] = min(leftchild, rightchild)
    return seg_tree[node]

def update(node,start,end,idx,val):
    if start == end:
        seg_tree[node] = val
        return
    mid = (start+end)//2
    if idx <= mid :
        update(node*2,start,mid,idx,val)
    else :
        update(node*2+1,mid+1,end,idx,val)
    seg_tree[node] = min(seg_tree[node*2], seg_tree[node*2+1])
    return

def query(left, right, node, start, end):
    if left > end or right < start:
        return 1e9+1
    if left <= start and end <= right:
        return seg_tree[node]
    mid = (start + end) // 2
    leftchild = query(left, right, node * 2, start, mid)
    rightchild = query(left, right, node * 2 + 1, mid + 1, end)
    return min(leftchild, rightchild)

N = int(input())
lis = list(map(int,input().split()))
M = int(input())
seg_tree = [(1e9, 0)] * (N * 4)

init(0, N - 1, 1)
for _ in range(M):
    n1, n2 ,n3= map(int, input().split())
    if n1 == 1 :
        update(1,0,len(lis)-1,n2-1,n3)
    else :
        print(query(n2-1,n3-1,1,0,len(lis)-1))
